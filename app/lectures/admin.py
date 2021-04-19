from django.contrib import admin

from .models import Lecture


class LectureAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "subject")
    search_fields = ("title", "created_by__email", "subject_ _title")


admin.site.register(Lecture, LectureAdmin)
