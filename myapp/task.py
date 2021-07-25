from celery.decorators import task
from celery.utils.log import  get_task_logger
from time import sleep

from celery import shared_task

from django.http import HttpResponse

logger = get_task_logger(__name__)

@task(name="my_first_task")
def my_first_task(duration):
    sleep(duration)
    print("first task done")
    return('first_task_done')

@task(name="adding_task")
def adding_task(x,y):
    return x+y