from django.contrib.auth import get_user_model
from rest_framework import serializers
from study_groups.serializers import StudyGroupSerializer

from .models import User, UserProfile, InstructorProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", "is_instructor", "is_student")
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    group = StudyGroupSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("user", "first_name", "last_name", "group")


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    group = serializers.IntegerField()

    def create(self, validated_data):
        return User.objects.create_with_profile(email=validated_data["email"],
                                                password=validated_data["password"],
                                                first_name=validated_data["first_name"],
                                                last_name=validated_data["last_name"],
                                                group_id=validated_data["group"])

    def update(self, instance, validated_data):
        pass


class InstructorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorProfile
        fields = "__all__"
