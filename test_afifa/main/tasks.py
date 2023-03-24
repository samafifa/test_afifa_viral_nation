import pymongo.errors
import requests
import json

import traceback
from django.db import IntegrityError
from celery import shared_task

from main.models import Users
from main.mongodb import users


@shared_task()
def add_users_to_db():
    response = requests.get(url="https://fakestoreapi.com/users", verify=False)

    if response.status_code == 200:
        data = json.loads(response.text)

        user_created = False
        for d in data:
            if not Users.objects.filter(username=d['username']).exists():
                # to make operation thread safe check for already existing user
                # if Integrity exception raised user already created
                # by another thread
                try:
                    user = Users.objects.create(
                        username=d['username'],
                        password=d['password'],
                        firstname=d['name']['firstname'],
                        lastname=d['name']['lastname'],
                        address=d['address'],
                        phonenumber=d['phone']
                    )
                except IntegrityError:
                    traceback.print_exc()
                else:
                    user_created = True

                # check if user was created
                if user_created:
                    try:
                        # check if user already exists
                        u = users.find_one({"id": user.id})

                        if u is None:
                            users.insert_one({
                                "id": user.id,
                                "username": d['username'],
                                "password": d['password'],
                                "firstname": d['name']['firstname'],
                                "lastname": d['name']['lastname'],
                                "address": d['address'],
                                "phonenumber": d['phone']
                            })
                    except pymongo.errors.DuplicateKeyError:
                        traceback.print_exc()

                user_created = False

