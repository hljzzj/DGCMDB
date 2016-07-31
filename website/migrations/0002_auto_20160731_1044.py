# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerHostRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='serverhost',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='serverhost',
            name='status',
            field=models.ForeignKey(related_name='status_status', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe7\x8a\xb6\xe6\x80\x81', to='website.DeviceStatus'),
        ),
        migrations.AddField(
            model_name='serverhostrecord',
            name='hostIP',
            field=models.ForeignKey(related_name='hostIP_hostIP', verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8IP', to='website.ServerHost', null=True),
        ),
        migrations.AddField(
            model_name='serverhostrecord',
            name='hostName',
            field=models.ForeignKey(related_name='hostName_hostName', verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x90\x8d\xe5\xad\x97', to='website.ServerHost', null=True),
        ),
        migrations.AddField(
            model_name='serverhostrecord',
            name='status',
            field=models.ForeignKey(related_name='status1_status1', verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\x8a\xb6\xe6\x80\x81', to='website.DeviceStatus', null=True),
        ),
    ]
