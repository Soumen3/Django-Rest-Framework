from django.contrib import admin
from .models import Student

# Register your models here.
# admin.sight.register(Student)

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
    search_fields = ['id']