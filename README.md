# airflow-data-pipeline

## Introduction

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

![Airflow DAG](dag.png)

## Getting started


### Project structure explanation
```
postgres-data-modeling
│   README.md                # Project description
│   docker-compose.yml       # Postgres container description   
│
└───data                     # The dataset
|   |               
│   └───log_data
│   |   │  ...
|   └───song_data
│       │  ...
│   
└───src                     # Source code
|   |               
│   └───notebooks           # Jupyter notebooks
│   |   │  etl.ipynb        # ETL helper notebook
|   |   |  test.ipynb       # Psql queries notebook
|   |   |
|   └───scripts
│       │  create_tables.py # Schema creation script
|       |  etl.py           # ETL script
|       |  sql_queries.py   # Definition of all sql queries
```

#### Requirements

* Install [Python3](https://www.python.org/downloads/)
* Install [Docker](https://www.docker.com/)
* Install [Docker Compose](https://docs.docker.com/compose/install/)
* [AWS](https://aws.amazon.com/) account and [Redshift](https://aws.amazon.com/redshift/) cluster 

#### Clone repository to local machine
```
git clone https://github.com/brfulu/postgres-data-modeling.git
```

#### Change directory to local repository
```
cd postgres-data-modeling
```

#### Create python virtual environment
```
python3 -m venv venv             # create virtualenv
source venv/bin/activate         # activate virtualenv
pip install -r requirements.txt  # install requirements
```


#### Start Airflow container
```
docker-compose up
```

#### Visit the Airflow UI
Go to http://localhost:8080

Username: user 

Password: password