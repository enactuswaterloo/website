# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20150526_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='link',
            field=models.URLField(default=None, max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
