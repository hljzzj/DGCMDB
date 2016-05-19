from django.db import models
# _*_ coding: utf-8 _*_

# Create your models here.

class SiteInfo(models.Model):       #websiteconfig
    SiteName = models.CharField(max_length=200)


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    worknameid = models.CharField(max_length=50)
    CreateDate = models.DateField(auto_created=)
    Logintime = models.DateTimeField(default='2016-12-12 12:12')
    LoginIP = models.CharField(max_length=16)
    Super = models.IntegerField(default='1')

class UserSuper(models.Model):
    supername = models.CharField(max_length=50)

class danwei(models.Model):
    workname = models.CharField(max_length=50)



class IPInfo(models.Model):

    worknameid = models.IntegerField(default='1')
    IP = models.GenericIPAddressField(protocol='ipv4')