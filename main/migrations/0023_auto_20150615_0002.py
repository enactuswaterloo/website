# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20150601_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverpic',
            name='url',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
