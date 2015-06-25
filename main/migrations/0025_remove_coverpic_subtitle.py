# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20150615_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverpic',
            name='subtitle',
        ),
    ]
