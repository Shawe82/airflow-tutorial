from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.docker_operator import DockerOperator

# Airflow connection ids
DOCKER_REGISTRY = "SHAWE_REGISTRY"

REGISTRY = ""

# Airflow variables
HOST_DIR = "share-dir"
TAG = "dummy-elt-tag"

# Constants
OUTPUT_DIR = "/usr/local/shawe/share"


# Here the actual dag is defined
default_args = {
    "start_date": datetime(2019, 3, 18),
    "owner": "shawe",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG("elt-dummy-tutorial-complex", default_args=default_args, schedule_interval="@daily") as dag:
    # Volumes mounted to the docker container
    volumes = [f"{Variable.get(HOST_DIR)}:{OUTPUT_DIR}"]
    # Tag determined from variable hosted in airflow. if not set, it defaults to latest
    image_tag = Variable.get(TAG, default_var="latest")
    def make_etl_operator(task_id : str, operation : str):
        cmd = f"'etl --out-dir {OUTPUT_DIR} {operation}'"
        return DockerOperator(
            api_version="auto",
            docker_conn_id=DOCKER_REGISTRY,
            environment={"PYTHONUNBUFFERED": 1},
            task_id=task_id,
            image=f"{REGISTRY}etl-dummy:{image_tag}",
            command=cmd,
            volumes=volumes,
            auto_remove=True,
        )

    extract = make_etl_operator("extract-step-dummy-etl", "extract")
    transform = make_etl_operator("transform-step-dummy-etl", "transform")
    load = make_etl_operator("load-step-dummy-etl", "load")

    extract >> transform >> load
