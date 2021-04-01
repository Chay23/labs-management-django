from django.contrib import admin

from .models import UserProfile, User, InstructorProfile

admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(InstructorProfile)
