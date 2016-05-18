# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='danwei',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IPInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IP', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('WorkGroup', models.CharField(max_length=50)),
                ('CreateDate', models.DateTimeField(default=b'2016-12-12 12:12')),
                ('Logintime', models.DateTimeField(default=b'2016-12-12 12:12')),
                ('LoginIP', models.CharField(max_length=16)),
                ('Super', models.CharField(max_length=10)),
            ],
        ),
    ]
