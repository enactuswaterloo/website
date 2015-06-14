# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_delete_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverpic',
            name='text',
        ),
        migrations.AddField(
            model_name='coverpic',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'coverpics/'),
        ),
        migrations.AddField(
            model_name='coverpic',
            name='link',
            field=models.CharField(default=b'/', max_length=200),
        ),
        migrations.AddField(
            model_name='coverpic',
            name='subtitle',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'projects/images/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='shortDesc',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
