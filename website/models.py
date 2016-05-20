#coding=utf-8
from django.db import models
# Create your models here.
#站点配置
class SiteInfo(models.Model):
    SiteName = models.CharField(max_length=200)

#日志
class Logexer(models.Model):        #操作日志
    time = models.DateTimeField(verbose_name='操作时间')
    name = models.CharField(max_length=20,verbose_name='操作人')
    ip = models.CharField(max_length=30,verbose_name='操作IP')
    act = models.CharField(max_length=200,verbose_name='操作行为')
class Logbrowse(models.Model):      #访问记录
    time = models.DateTimeField(verbose_name='访问时间')
    ip = models.CharField(max_length=30,verbose_name='访问IP')
    act = models.CharField(max_length=200,verbose_name='访问行为')

#用户信息配置
class UserInfo(models.Model):
    username = models.CharField(max_length=50,verbose_name='用户名称')
    password = models.CharField(max_length=50,verbose_name='用户密码')
    work = models.CharField(max_length=50,verbose_name='部门')
    CreateDate = models.DateField(max_length=50,verbose_name='用户创建时间')
    Logintime = models.DateTimeField(default='2016-12-12 12:12',verbose_name='用户登陆时间')
    LoginIP = models.CharField(max_length=16,verbose_name='用户登陆IP')
    Super = models.IntegerField(default='1',verbose_name='用户权限')
#用户权限表
class UserSuper(models.Model):
    supername = models.CharField(max_length=50)
#部门表
class Work(models.Model):
    work = models.CharField(max_length=50)



class IPInfo(models.Model):

    worknameid = models.IntegerField(default='1')
    IP = models.GenericIPAddressField(protocol='ipv4')