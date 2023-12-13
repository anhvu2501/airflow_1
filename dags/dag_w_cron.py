from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'vuhta',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_cron_expressions_v3',
    default_args=default_args,
    start_date=datetime(2023, 12, 1),
    schedule_interval='0 0 * * Tue-Fri',
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a dag with cron job!'
    )