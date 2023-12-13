from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'vuhta',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='my_first_dag_v3',
    default_args=default_args,
    description='this is my first dag',
    start_date=datetime(2023, 12, 10, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command='echo hello world. this is the first airflow dag'
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command='echo hey this is the second task executed after task 1'
    )

    task3 = BashOperator(
        task_id = 'third_task',
        bash_command='echo hey this is the third task executed after task 1 and at the same time with task 2'
    )

    # Task dependency 1
    task1.set_downstream(task2)
    task1.set_downstream(task3)

    # Task dependency 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency 3
    # task1 >> [task2, task3]