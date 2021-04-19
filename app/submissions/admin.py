from django.contrib import admin

from .models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("created_by", "attached_file", "assignment")
    search_fields = ("created_by__email", "attached_file", "assignment__title")


admin.site.register(Submission, SubmissionAdmin)
