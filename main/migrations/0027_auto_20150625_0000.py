# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20150624_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
