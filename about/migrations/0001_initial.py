# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public', models.BooleanField(default=False)),
                ('picture', models.ImageField(default=None, null=True, upload_to=b'member-pics/', blank=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('program', models.CharField(default=b'Accounting and Financial Management', max_length=150)),
                ('year', models.CharField(default=b'2019', max_length=100)),
                ('position', models.CharField(default=b'Member', max_length=100)),
                ('bio', models.TextField(max_length=400, blank=True)),

            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
