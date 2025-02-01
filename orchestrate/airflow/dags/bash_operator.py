import json
import logging
import os
import subprocess
from collections.abc import Iterable
import datetime
import pendulum
from airflow import DAG

try:
    from airflow.operators.bash_operator import BashOperator
    from airflow.operators.empty import EmptyOperator
except ImportError:
    from airflow.operators.bash import BashOperator

from pathlib import Path

local_tz = pendulum.timezone("America/Sao_Paulo")

DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2025,1,31, 00,30),
    'retries': 1,
}

with DAG(
    dag_id="extract",
    schedule_interval='0 * * * *',
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=10),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
    default_args=DEFAULT_ARGS.copy()
) as dag:
    task1 = BashOperator(
        task_id="bash_task",
        bash_command="echo \"here is the message: '$message'\"",
        env={"message": 'task1'},
    )
    task2 = BashOperator(
        task_id="bash_task",
        bash_command="echo \"here is the message: '$message'\"",
        env={"message": 'task2'},
    )
    run_this_last = BashOperator(
        task_id="bash_task",
        bash_command="echo \"here is the message: '$message'\"",
        env={"message": 'last'},
    )

    [t1,t2] >> run_this_last



