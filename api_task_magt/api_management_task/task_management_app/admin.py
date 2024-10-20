from django.contrib import admin

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Task

# Customizing the Admin Site
admin.site.site_header = "Task Management API Admin"
admin.site.site_title = "Admin Portal For Task Management API "
admin.site.index_title = "Welcome to the Task Management Dashboard"

# Registering models
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'due_date', 'created_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'priority')

