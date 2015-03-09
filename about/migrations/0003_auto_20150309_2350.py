# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_person_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
