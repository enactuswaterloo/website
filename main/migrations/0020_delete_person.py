# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20150301_0605'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
