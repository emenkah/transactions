from celery import shared_task
from time import sleep

@shared_task
def sleepy():
    sleep(10)
    print("Done in sleepy function from tasks")
    return None
