from django.db import models


class Users(models.Model):
    class Meta:
        db_table = 'users'

    id = models.AutoField(primary_key=True)
    address = models.JSONField(default=None, null=True)
    username = models.CharField(max_length=140, default=None, null=True)
    password = models.CharField(max_length=255, default=None, null=True)
    firstname = models.CharField(max_length=140, default='Unknown', null=True)
    lastname = models.CharField(max_length=140, default=None, null=True)
    phonenumber = models.CharField(max_length=25, default=None, null=True)
