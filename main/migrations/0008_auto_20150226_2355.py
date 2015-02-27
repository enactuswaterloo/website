# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_person_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='firstName',
            field=models.CharField(default=b'N.', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='lastName',
            field=models.CharField(default=b'Actus', max_length=100),
            preserve_default=True,
        ),
    ]
