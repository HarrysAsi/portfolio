from django.contrib import admin

from apps.skills.models import ToolType, Tool

admin.site.register(Tool)
admin.site.register(ToolType)
