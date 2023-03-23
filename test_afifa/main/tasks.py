import requests
import json

from celery import shared_task

from main.models import Users
from main.mongodb import users


@shared_task()
def add_users_to_db():
    response = requests.get(url="https://fakestoreapi.com/users", verify=False)

    if response.status_code == 200:
        data = json.loads(response.text)

        for d in data:
            if not Users.objects.filter(username=d['username']).exists():
                Users.objects.create(
                    username=d['username'],
                    password=d['password'],
                    firstname=d['name']['firstname'],
                    lastname=d['name']['lastname'],
                    address=d['address'],
                    phonenumber=d['phone']
                )

