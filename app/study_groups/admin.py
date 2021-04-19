from django.contrib import admin

from .models import StudyGroup


class GroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(StudyGroup, GroupAdmin)
