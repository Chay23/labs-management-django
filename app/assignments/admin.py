from django.contrib import admin

from .models import Assignment


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "subject")
    search_fields = ("title", "created_by__email", "subject__title")


admin.site.register(Assignment, AssignmentAdmin)
