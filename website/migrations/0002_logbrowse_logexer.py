# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-20 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logbrowse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe6\x97\xb6\xe9\x97\xb4')),
                ('ip', models.CharField(max_length=30, verbose_name=b'\xe8\xae\xbf\xe9\x97\xaeIP')),
                ('act', models.CharField(max_length=200, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe8\xa1\x8c\xe4\xb8\xba')),
            ],
        ),
        migrations.CreateModel(
            name='Logexer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe4\xba\xba')),
                ('ip', models.CharField(max_length=30, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9cIP')),
                ('act', models.CharField(max_length=200, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe8\xa1\x8c\xe4\xb8\xba')),
            ],
        ),
    ]