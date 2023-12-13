from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'vuhta',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# ti: task instance
def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f'Hello world!. My name is {first_name} {last_name} and I am {age} years old')

def get_name(ti):
    ti.xcom_push(key='first_name', value='Vu')
    ti.xcom_push(key='last_name', value='Ho Tran Anh')

def get_age(ti):
    ti.xcom_push(key='age', value='20')

with DAG(
    default_args=default_args,
    dag_id='first_dag_python_operator_v6',
    description='First dag using python operator',
    start_date=datetime(2023, 12, 10),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
        # op_kwargs={'age': 22}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1