from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator

default_args = {
    "owner": "Ice",
    "start_date": timezone.datetime(2021, 9, 29)
}

with DAG(
    "home_work_1",
    schedule_interval="*/10 * * * *",
    default_args=default_args,
    catchup=False,
    tags=["saksiam"],
) as dag:

    one = DummyOperator(task_id="1")
    two = DummyOperator(task_id="2")
    three = DummyOperator(task_id="3")
    four = DummyOperator(task_id="4")
    five = DummyOperator(task_id="5")
    six = DummyOperator(task_id="6")
    seven = DummyOperator(task_id="7")
    eight = DummyOperator(task_id="8")
    nine = DummyOperator(task_id="9")
 
    one >> [two, five]
    two >> [three, six]
    three >> four
    [four, eight] >> nine
    five >> [six, seven] >> eight