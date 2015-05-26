# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_person_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='link',
            field=models.URLField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
