# afimage
FROM puckel/docker-airflow:1.10.4
# We need to be root and run the container with the --priveleged flag on in order to execute docker.
# Another option would be groupadd --gid 999 docker && usermod -aG docker airflow, however, we do not
# know, if the gid is the correct one. Both version seem to be a bit hackey but need to see how to resolve that.
USER root
RUN pip install -U pip \
&& pip install docker
#&& groupadd --gid 999 docker \
#&& usermod -aG docker airflow

#RUN sed -i 's/LocalExecutor/SequentialExecutor/' /entrypoint.sh

#USER airflow
ENV SHARE_DIR /usr/local/share

