from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.operators.dummy_operator import DummyOperator
from operators import (StageToRedshiftOperator, LoadFactOperator,
                       LoadDimensionOperator, DataQualityOperator, CreateRedshiftTableOperator)
from helpers import SqlQueries

# aws_hook = AwsHook("aws_credentials")
# print(aws_hook.aws_conn_id)
# credentials = aws_hook.get_credentials()
# print(credentials)

default_args = {
    'owner': 'brfulu',
    'start_date': datetime(2019, 1, 12),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': 300,
    'email_on_retry': False
}

dag = DAG('s3_to_redshift_dag',
          default_args=default_args,
          description='Extract Load and Transform data from S3 to Redshift',
          schedule_interval='@daily',
          catchup=False
          )

start_operator = DummyOperator(task_id='Begin_execution', dag=dag)

create_events_table = CreateRedshiftTableOperator(
    task_id='Create_events_table',
    dag=dag
)

create_songs_table = CreateRedshiftTableOperator(
    task_id='Create_songs_table',
    dag=dag
)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    dag=dag
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Stage_songs',
    dag=dag
)

load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    dag=dag
)

load_user_dimension_table = LoadDimensionOperator(
    task_id='Load_user_dim_table',
    dag=dag
)

load_song_dimension_table = LoadDimensionOperator(
    task_id='Load_song_dim_table',
    dag=dag
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id='Load_artist_dim_table',
    dag=dag
)

load_time_dimension_table = LoadDimensionOperator(
    task_id='Load_time_dim_table',
    dag=dag
)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag
)

end_operator = DummyOperator(task_id='Stop_execution', dag=dag)

# DAG dependencies
start_operator >> create_songs_table
start_operator >> create_events_table

create_songs_table >> stage_songs_to_redshift
create_events_table >> stage_events_to_redshift

stage_events_to_redshift >> load_songplays_table
stage_songs_to_redshift >> load_songplays_table

load_songplays_table >> load_song_dimension_table
load_songplays_table >> load_user_dimension_table
load_songplays_table >> load_artist_dimension_table
load_songplays_table >> load_time_dimension_table

load_song_dimension_table >> run_quality_checks
load_user_dimension_table >> run_quality_checks
load_artist_dimension_table >> run_quality_checks
load_time_dimension_table >> run_quality_checks

run_quality_checks >> end_operator
