# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-20 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worknameid', models.IntegerField(default=b'1')),
                ('IP', models.GenericIPAddressField(protocol=b'ipv4')),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiteName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('password', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
                ('work', models.CharField(max_length=50, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8')),
                ('CreateDate', models.DateField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('Logintime', models.DateTimeField(default=b'2016-12-12 12:12', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x99\xbb\xe9\x99\x86\xe6\x97\xb6\xe9\x97\xb4')),
                ('LoginIP', models.CharField(max_length=16, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x99\xbb\xe9\x99\x86IP')),
                ('Super', models.IntegerField(default=b'1', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe6\x9d\x83\xe9\x99\x90')),
            ],
        ),
        migrations.CreateModel(
            name='UserSuper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supername', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=50)),
            ],
        ),
    ]
