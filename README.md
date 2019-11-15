# airflow-tutorial
Tutorial code for how to deploy airflow using docker and how to use the DockerOperator.

To run the example, you first have to  build the image in etl-dummy. Just do
```
docker build -t etl-dummy ./etl-dummy
``` 

Now, you can start the Airflow instance using
```
docker-compose up
``` 

This should build the airflow image when you execute it the first time and also starts the airflow server. Now you
 should be ready to go a play around with it.

For further details, refer to my 
[medium](https://medium.com/@simon.hawe/how-to-use-airflow-without-headaches-4e6e37e6c2bc) article.
