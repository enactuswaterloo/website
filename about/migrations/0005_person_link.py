# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20150310_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='link',
            field=models.URLField(default=False, max_length=150),
            preserve_default=True,
        ),
    ]
