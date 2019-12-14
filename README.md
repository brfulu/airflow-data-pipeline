# airflow-data-pipeline

## Requirements

* Install [Python3](https://www.python.org/downloads/)
* Install [Docker](https://www.docker.com/)
* Install [Docker Compose](https://docs.docker.com/compose/install/)

#### Start Airflow container
```
# set airflow home variable
export AIRFLOW_HOME=`pwd`/airflow

# install requirements
pip install -r requirements.txt

# initialize the database
airflow initdb

# start the Airflow UI webserver
airflow webserver -p 8080

# start the scheduler
airflow scheduler
```
#### Visit the Airflow UI
Go to http://localhost:8080