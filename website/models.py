from django.db import models


# Create your models here.

class SiteInfo(models.Model):
    SiteName = models.CharField(max_length=200)


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    WorkGroup = models.CharField(max_length=50)
    CreateDate = models.DateTimeField(default='2016-12-12 12:12')
    Logintime = models.DateTimeField(default='2016-12-12 12:12')
    LoginIP = models.CharField(max_length=16)
    Super = models.CharField(max_length=10)


class IPInfo(models.Model):
    IP = models.CharField(max_length=50)

class danwei(models.Model):
    workname = models.CharField(max_length=50)

