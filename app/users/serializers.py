from django.contrib.auth import get_user_model
from rest_framework import serializers
from study_groups.serializers import StudyGroupSerializer

from .models import UserProfile, InstructorProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "is_instructor", "is_student")


class UserProfileSerializer(serializers.ModelSerializer):
    group = StudyGroupSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("user", "first_name", "last_name", "group")


class InstructorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorProfile
        fields = "__all__"
