# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150226_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default=b'N. Actus', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.CharField(default=b'smiley_face.jpg', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(default=b'Member', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='program',
            field=models.CharField(default=b'Currently failing', max_length=100),
            preserve_default=True,
        ),
    ]
