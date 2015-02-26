# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150226_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='year',
            field=models.CharField(default=b'2019', max_length=100),
            preserve_default=True,
        ),
    ]
