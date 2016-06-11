# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_logbrowse_logexer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyCateInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ApplyType', models.IntegerField(verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('IDCard', models.IntegerField(verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81')),
                ('Workgroup', models.IntegerField(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x8d\x95\xe4\xbd\x8d')),
                ('UserName', models.CharField(max_length=b'50', null=b'Ture', verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('UserSex', models.IntegerField(verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('UserPhone', models.IntegerField(verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('UserIDCard', models.IntegerField(verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81')),
                ('UserEmail', models.EmailField(max_length=254, verbose_name=b'\xe7\x94\xb5\xe5\xad\x90\xe9\x82\xae\xe4\xbb\xb6')),
                ('UserAddress', models.CharField(max_length=b'50', verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('Userzhiwu', models.IntegerField(verbose_name=b'\xe4\xbb\xbb\xe8\x81\x8c')),
                ('UserLeve', models.IntegerField(verbose_name=b'\xe8\x81\x8c\xe7\xba\xa7')),
                ('UserWork', models.IntegerField(verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xb2\x97\xe4\xbd\x8d')),
                ('UserWrokType', models.IntegerField(verbose_name=b'\xe8\xad\xa6\xe7\xa7\x8d')),
                ('UserApplyTime', models.DateTimeField(verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4')),
                ('UserCateID', models.CharField(max_length=b'50', verbose_name=b'\xe8\xaf\x81\xe4\xb9\xa6\xe7\xbc\x96\xe5\x8f\xb7')),
                ('UserIP', models.IPAddressField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6IP')),
            ],
        ),
        migrations.CreateModel(
            name='AssetsClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assetsclass', models.CharField(max_length=50, verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7\xe5\x88\x86\xe7\xb1\xbb')),
            ],
        ),
        migrations.CreateModel(
            name='AssetsWalkie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Wid', models.IntegerField(max_length=4, verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe7\xbc\x96\xe5\x8f\xb7')),
                ('walkiemodel', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('number', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe6\x95\xb0\xe9\x87\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='computercate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OutAssetsWalkie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('outstocktime', models.DateTimeField(verbose_name=b'\xe5\x87\xba\xe5\xba\x93\xe6\x97\xb6\xe9\x97\xb4')),
                ('Wid', models.IntegerField(max_length=4, verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe7\xbc\x96\xe5\x8f\xb7')),
                ('walkiemodel', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('number', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe6\x95\xb0\xe9\x87\x8f')),
                ('outtype', models.IntegerField(verbose_name=b'\xe5\x87\xba\xe5\xba\x93\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('work', models.IntegerField(verbose_name=b'\xe9\xa2\x86\xe7\x94\xa8\xe9\x83\xa8\xe9\x97\xa8')),
                ('Recipient', models.CharField(max_length=20, verbose_name=b'\xe9\xa2\x86\xe7\x94\xa8\xe4\xba\xba')),
                ('phone1', models.CharField(max_length=11, verbose_name=b'\xe4\xbf\xa1\xe7\x94\xa8\xe4\xba\xba\xe7\x94\xb5\xe8\xaf\x9d')),
                ('administrator', models.CharField(max_length=20, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98')),
                ('phone2', models.CharField(max_length=11, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98\xe7\x94\xb5\xe8\xaf\x9d')),
                ('charger', models.IntegerField(verbose_name=b'\xe5\x85\x85\xe7\x94\xb5\xe5\x99\xa8\xe6\x95\xb0\xe9\x87\x8f')),
                ('headset', models.IntegerField(verbose_name=b'\xe8\x80\xb3\xe9\xba\xa6\xe6\x95\xb0\xe9\x87\x8f')),
                ('walkiereturn', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xbd\x92\xe8\xbf\x98')),
            ],
        ),
        migrations.CreateModel(
            name='OutType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('outtype', models.CharField(max_length=20, verbose_name=b'\xe5\x87\xba\xe5\xba\x93\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
        ),
        migrations.CreateModel(
            name='StorageAssetsWalkie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Wid', models.IntegerField(max_length=4, verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe7\xbc\x96\xe5\x8f\xb7')),
                ('walkiemodel', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('number', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe6\x95\xb0\xe9\x87\x8f')),
                ('storagetime', models.DateTimeField(verbose_name=b'\xe5\x85\xa5\xe5\xba\x93\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='WalkieModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('walkiemodel', models.CharField(max_length=20, verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe5\x9e\x8b\xe5\x8f\xb7')),
            ],
        ),
        migrations.CreateModel(
            name='workcate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workcate', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='password',
            new_name='pwd',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='username',
            new_name='user',
        ),
    ]
