# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20150309_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(related_name='profile', null=True, default=None, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
