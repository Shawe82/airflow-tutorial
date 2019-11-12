# afimage
FROM puckel/docker-airflow:1.10.4
# We need to be root and run the container with the --priveleged flag on in order to execute docker.
# Another option would be groupadd --gid 999 docker && usermod -aG docker airflow, however, we do not
# know, if the gid is the correct one. Both version seem to be a bit hackey but need to see how to resolve that.
USER root
ARG AIRFLOW_HOME=/usr/local/airflow
RUN pip install docker
ENV SHARE_DIR /usr/local/share
COPY ./config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
#COPY ./dags ${AIRFLOW_HOME}/dags

