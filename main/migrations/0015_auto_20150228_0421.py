# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20150228_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='firstName',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='lastName',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='program',
            field=models.CharField(default=b'Accounting and Financial Management', max_length=150),
            preserve_default=True,
        ),
    ]
