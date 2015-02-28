# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150228_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.ImageField(default=b'smiley_face.jpg', upload_to=b'media/member-pics/'),
            preserve_default=True,
        ),
    ]
