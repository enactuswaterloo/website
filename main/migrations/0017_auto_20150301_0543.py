# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150301_0516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
