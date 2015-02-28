# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150228_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.ImageField(default=b'member-pics/smiley_face.jpg', upload_to=b'member-pics/'),
            preserve_default=True,
        ),
    ]
