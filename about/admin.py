from django.contrib import admin
from about.models import Person

# Register your models here.
def approve_person(modeladmin, request, queryset):
	queryset.update(approved=True)

approve_person.short_description = "Approve selected users"

class PersonAdmin (admin.ModelAdmin):
	list_display = ['user', 'position', 'approved']
	ordering = ['-priority']
	actions = [approve_person]

admin.site.register(Person, PersonAdmin)