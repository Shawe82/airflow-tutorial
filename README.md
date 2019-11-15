# airflow-tutorial
Tutorial like code for how to deploy airflow using docker and how to use the DockerOperator.

To run the example, you first have to  build the image in etl-dummy. Just do
```
docker build -t etl-dummy ./etl-dummy
``` 

Now, you can start the Airflow instance using
```
docker-compose up
``` 

This should build the airflow image when you execute it the first time and also start the airflow server.
To make the example actually work, you need to create a folder /usr/local/share/tmp_store_airflow with read and write
 permissions. 



For further details, refer to my 
[medium](https://medium.com/@simon.hawe/how-to-use-airflow-without-headaches-4e6e37e6c2bc) article.
