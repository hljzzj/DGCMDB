# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160610_0405'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSuper',
            new_name='UserType',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='Super',
        ),
    ]
