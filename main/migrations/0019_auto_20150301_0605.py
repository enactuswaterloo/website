# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150301_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(max_length=400, blank=True),
            preserve_default=True,
        ),
    ]
