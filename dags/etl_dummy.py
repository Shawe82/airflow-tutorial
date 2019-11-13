from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.docker_operator import DockerOperator

# Constants
OUTPUT_DIR = "/usr/local/shawe/share"

# Here the actual dag is defined
default_args = {
    "start_date": datetime(2019, 11, 13),
    "owner": "shawe",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG("elt-dummy-tutorial", default_args=default_args, schedule_interval="@hourly") as dag:
    # Volumes mounted to the docker container
    def make_etl_operator(task_id: str, operation: str):
        cmd = f"'etl --out-dir {OUTPUT_DIR} {operation}'"
        return DockerOperator(
            command=cmd,
            environment={"PYTHONUNBUFFERED": 1},
            task_id=task_id,
            image=f"etl-dummy:latest",
            volumes=[f"/usr/local/share:{OUTPUT_DIR}"],
            auto_remove=True,
        )


    extract = make_etl_operator("extract-step-dummy-etl", "extract")
    transform = make_etl_operator("transform-step-dummy-etl", "transform")
    load = make_etl_operator("load-step-dummy-etl", "load")

extract >> transform >> load
