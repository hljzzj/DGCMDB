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


#工作记录
class workcate(models.Model):       #工作分类
    workcate = models.CharField(max_length=50)

class computercate(models.Model):       #计算机工作表
    work = models.IntegerField()


#资产管理

class AssetsClass(models.Model):
    assetsclass = models.CharField(max_length=50,verbose_name='资产分类')


class AssetsWalkie(models.Model):       #对讲机库存
    Wid = models.IntegerField(max_length=4,verbose_name='对讲机编号')
    walkiemodel = models.IntegerField(verbose_name='对讲机型号')
    number = models.IntegerField(verbose_name='对讲机数量')

class OutAssetsWalkie(models.Model):        #对讲机外出
    outstocktime = models.DateTimeField(verbose_name='出库时间')
    Wid = models.IntegerField(max_length=4,verbose_name='对讲机编号')
    walkiemodel = models.IntegerField(verbose_name='对讲机型号')
    number = models.IntegerField(verbose_name='对讲机数量')
    outtype = models.IntegerField(verbose_name='出库类型')
    work = models.IntegerField(verbose_name='领用部门')
    Recipient = models.CharField(max_length=20,verbose_name='领用人')
    phone1 = models.CharField(max_length=11, verbose_name='信用人电话')
    administrator = models.CharField(max_length=20,verbose_name='管理员')
    phone2 = models.CharField(max_length=11,verbose_name='管理员电话')
    charger = models.IntegerField(verbose_name='充电器数量')
    headset = models.IntegerField(verbose_name='耳麦数量')
    walkiereturn = models.BooleanField(verbose_name="是否归还")
class StorageAssetsWalkie(models.Model):     #对讲机入库
    Wid = models.IntegerField(max_length=4,verbose_name='对讲机编号')
    walkiemodel = models.IntegerField(verbose_name='对讲机型号')
    number = models.IntegerField(verbose_name='对讲机数量')
    storagetime = models.DateTimeField(verbose_name='入库时间')


class WalkieModel(models.Model):
    walkiemodel = models.CharField(max_length=20,verbose_name='对讲机型号')

class OutType(models.Model):
    outtype = models.CharField(max_length=20,verbose_name='出库类型')