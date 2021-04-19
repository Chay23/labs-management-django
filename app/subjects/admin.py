from django.contrib import admin

from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by")
    search_fields = ("title", "created_by__email")


admin.site.register(Subject, SubjectAdmin)
