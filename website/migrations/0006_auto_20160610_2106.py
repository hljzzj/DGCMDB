# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20160610_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=256)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='logbrowse',
            name='ip',
            field=models.IPAddressField(verbose_name=b'\xe8\xae\xbf\xe9\x97\xaeIP'),
        ),
        migrations.AlterField(
            model_name='logbrowse',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='logexer',
            name='act',
            field=models.CharField(max_length=256, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe8\xa1\x8c\xe4\xb8\xba'),
        ),
        migrations.AlterField(
            model_name='logexer',
            name='ip',
            field=models.IPAddressField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9cIP'),
        ),
        migrations.AlterField(
            model_name='logexer',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe4\xba\xba'),
        ),
        migrations.AlterField(
            model_name='logexer',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='CreateDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', error_messages={b'invalid': b'\xe6\x97\xa5\xe6\x9c\x9f\xe6\xa0\xbc\xe5\xbc\x8f\xe9\x94\x99\xe8\xaf\xaf'}),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='LoginIP',
            field=models.IPAddressField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x99\xbb\xe9\x99\x86IP'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Logintime',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x99\xbb\xe9\x99\x86\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
