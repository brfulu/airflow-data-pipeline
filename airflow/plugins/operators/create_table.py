from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook


class CreateRedshiftTableOperator(BaseOperator):
    ui_color = '#9A8ECC'

    @apply_defaults
    def __init__(self,
                 *args, **kwargs):
        super(CreateRedshiftTableOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        self.log.info('StageToRedshiftOperator not implemented yet')
