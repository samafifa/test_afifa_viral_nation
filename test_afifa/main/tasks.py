import requests
import json

from celery import shared_task


@shared_task()
def add_users_to_db(count):
    response = requests.get(url="https://fakestoreapi.com/users", verify=False)

    if response.status_code == 200:
        data = json.loads(response.text)
