# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20150531_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverpic',
            name='link',
        ),
        migrations.AlterField(
            model_name='coverpic',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
