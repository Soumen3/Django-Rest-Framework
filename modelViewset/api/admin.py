from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'roll', 'city', 'marks']
	list_display_links = ['name']
	search_fields = ['name', 'city']
	list_filter = ['city']
	list_editable = ['marks']