# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.template.defaultfilters import slugify

def slugify_titles(apps, schema_editor):
    Project = apps.get_model("main","Project")
    for project in Project.objects.all():
        project.slug = slugify(project.title)
        project.save()

def remove_slugs(apps, schema_editor):
    Project = apps.get_model("main","Project")
    for project in Project.objects.all():
        project.slug = None
        project.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_project_slug'),
    ]

    operations = [
        migrations.RunPython(slugify_titles, remove_slugs)
    ]
