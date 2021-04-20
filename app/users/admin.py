from django.contrib import admin

from .models import UserProfile, User, InstructorProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_admin", "is_student", "is_instructor")
    search_fields = ("email",)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "group")
    search_fields = ("user__email", "first_name", "last_name", "group__name",)


class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name")
    search_fields = ("user__email", "first_name", "last_name",)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(InstructorProfile, InstructorProfileAdmin)
