from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook


class StageToRedshiftOperator(BaseOperator):
    ui_color = '#8EB6D4'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id='redshift',
                 aws_conn_id='aws_credentials',
                 table_name='unknown',
                 *args, **kwargs):
        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.aws_conn_id = aws_conn_id

    def execute(self, context):
        print(self.redshift_conn_id)
        print(self.aws_conn_id)

        aws_hook = AwsHook("aws_credentials")
        credentials = aws_hook.get_credentials()
        redshift_hook = PostgresHook("redshift")

        print(credentials)

        self.log.info('StageToRedshiftOperator not implemented yet')
