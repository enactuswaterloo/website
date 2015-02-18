# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150215_2311'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exec',
            new_name='Person',
        ),
    ]
