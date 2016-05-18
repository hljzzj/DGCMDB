from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    WorkGroup = models.CharField(max_length=50)
    CreateDate = models.DateTimeField()
    Logintime = models.DateTimeField()
    LoginIP = models.CharField(max_length=16)
    Super = models.CharField(max_length=10)


class IPInfo(models.Model):


class WorkGroup(models.Model):
    ID = models.IntegerField():
    WorkGroup = models.CharField(max_length=50)

