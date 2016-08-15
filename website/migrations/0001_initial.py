# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyCateInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UserName', models.CharField(max_length=50, null=b'Ture', verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('UserPhone', models.IntegerField(verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('UserIDCard', models.IntegerField(verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81')),
                ('UserEmail', models.EmailField(max_length=254, verbose_name=b'\xe7\x94\xb5\xe5\xad\x90\xe9\x82\xae\xe4\xbb\xb6')),
                ('UserAddress', models.CharField(max_length=50, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('UserApplyTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4')),
                ('UserCateID', models.CharField(max_length=50, null=True, verbose_name=b'\xe8\xaf\x81\xe4\xb9\xa6\xe7\xbc\x96\xe5\x8f\xb7')),
                ('UserIP', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6IP')),
            ],
        ),
        migrations.CreateModel(
            name='ApplyType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=256)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
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
                ('Wid', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe7\xbc\x96\xe5\x8f\xb7')),
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
            name='DeviceGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.CharField(max_length=50, null=True, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x88\x86\xe7\xbb\x84')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=50, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe7\x8a\xb6\xe6\x80\x81\xe5\x88\x86\xe7\xb1\xbb')),
            ],
        ),
        migrations.CreateModel(
            name='IPInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('worknameid', models.IntegerField(default=b'1')),
                ('IP', models.GenericIPAddressField(protocol=b'ipv4')),
            ],
        ),
        migrations.CreateModel(
            name='Logbrowse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe6\x97\xb6\xe9\x97\xb4')),
                ('ip', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'\xe8\xae\xbf\xe9\x97\xaeIP')),
                ('act', models.CharField(max_length=200, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe8\xa1\x8c\xe4\xb8\xba')),
            ],
        ),
        migrations.CreateModel(
            name='Logexer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe4\xba\xba')),
                ('ip', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9cIP')),
                ('act', models.CharField(max_length=256, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe8\xa1\x8c\xe4\xb8\xba')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deviceID', models.IntegerField(verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87ID')),
                ('deviceIP', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87IP')),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('group', models.ForeignKey(verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87\xe5\x88\x86\xe7\xbb\x84', to='website.DeviceGroup')),
                ('status', models.ForeignKey(verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87\xe7\x8a\xb6\xe6\x80\x81', to='website.DeviceStatus')),
            ],
        ),
        migrations.CreateModel(
            name='OutAssetsWalkie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('outstocktime', models.DateTimeField(verbose_name=b'\xe5\x87\xba\xe5\xba\x93\xe6\x97\xb6\xe9\x97\xb4')),
                ('Wid', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe7\xbc\x96\xe5\x8f\xb7')),
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
            name='ServerHostList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostName', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d\xe7\xa7\xb0')),
                ('hostIP', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xbaIP')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('group', models.ForeignKey(related_name='group_group', verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x88\x86\xe7\xbb\x84', to='website.DeviceGroup', null=True)),
                ('status', models.ForeignKey(related_name='status_status', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe7\x8a\xb6\xe6\x80\x81', to='website.DeviceStatus', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServerHostRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('hostIP', models.ForeignKey(related_name='hostIP_hostIP', verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8IP', to='website.ServerHostList', null=True)),
                ('status', models.ForeignKey(related_name='status1_status1', verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\x8a\xb6\xe6\x80\x81', to='website.DeviceStatus')),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SiteName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StorageAssetsWalkie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Wid', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe7\xbc\x96\xe5\x8f\xb7')),
                ('walkiemodel', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('number', models.IntegerField(verbose_name=b'\xe5\xaf\xb9\xe8\xae\xb2\xe6\x9c\xba\xe6\x95\xb0\xe9\x87\x8f')),
                ('storagetime', models.DateTimeField(verbose_name=b'\xe5\x85\xa5\xe5\xba\x93\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(unique=True, max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('pwd', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('work', models.CharField(max_length=50, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8')),
                ('CreateDate', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', error_messages={b'invalid': b'\xe6\x97\xa5\xe6\x9c\x9f\xe6\xa0\xbc\xe5\xbc\x8f\xe9\x94\x99\xe8\xaf\xaf'})),
                ('Logintime', models.DateTimeField(auto_now=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x99\xbb\xe9\x99\x86\xe6\x97\xb6\xe9\x97\xb4')),
                ('LoginIP', models.GenericIPAddressField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x99\xbb\xe9\x99\x86IP', protocol=b'ipv4')),
            ],
        ),
        migrations.CreateModel(
            name='UserLeve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe8\x81\x8c\xe7\xba\xa7')),
            ],
        ),
        migrations.CreateModel(
            name='UserSex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=4, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supername', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xb2\x97\xe4\xbd\x8d')),
            ],
        ),
        migrations.CreateModel(
            name='UserWorkType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe8\xad\xa6\xe7\xa7\x8d')),
            ],
        ),
        migrations.CreateModel(
            name='UserZhiWu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe4\xbb\xbb\xe8\x81\x8c')),
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
        migrations.CreateModel(
            name='WorkGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x8d\x95\xe4\xbd\x8d')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='typeId',
            field=models.ForeignKey(to='website.UserType'),
        ),
        migrations.AddField(
            model_name='applycateinfo',
            name='ApplyType',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe7\xb1\xbb\xe5\x9e\x8b', to='website.ApplyType'),
        ),
        migrations.AddField(
            model_name='applycateinfo',
            name='UserLeve',
            field=models.ForeignKey(verbose_name=b'\xe8\x81\x8c\xe7\xba\xa7', to='website.UserLeve'),
        ),
        migrations.AddField(
            model_name='applycateinfo',
            name='UserSex',
            field=models.ForeignKey(verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', to='website.UserSex'),
        ),
        migrations.AddField(
            model_name='applycateinfo',
            name='UserWork',
            field=models.ForeignKey(verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xb2\x97\xe4\xbd\x8d', to='website.UserWork'),
        ),
        migrations.AddField(
            model_name='applycateinfo',
            name='UserWrokType',
            field=models.ForeignKey(verbose_name=b'\xe8\xad\xa6\xe7\xa7\x8d', to='website.UserWorkType'),
        ),
        migrations.AddField(
            model_name='applycateinfo',
            name='Userzhiwu',
            field=models.ForeignKey(verbose_name=b'\xe4\xbb\xbb\xe8\x81\x8c', to='website.UserZhiWu'),
        ),
        migrations.AddField(
            model_name='applycateinfo',
            name='Workgroup',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x8d\x95\xe4\xbd\x8d', to='website.WorkGroup'),
        ),
    ]
