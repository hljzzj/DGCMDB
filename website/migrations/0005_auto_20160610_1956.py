# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20160610_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='typeId',
            field=models.ForeignKey(default=1, to='website.UserType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='CreateDate',
            field=models.DateTimeField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
