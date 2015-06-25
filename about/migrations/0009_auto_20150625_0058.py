# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_person_link_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(max_length=140, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='program',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]
