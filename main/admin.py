from django.contrib import admin
from main.models import Person, Coverpic, Project

# Register your models here.
admin.site.register(Person)
admin.site.register(Coverpic)
admin.site.register(Project)