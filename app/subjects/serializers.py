from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        validators = [UniqueTogetherValidator(
            queryset=Subject.objects.all(),
            fields=['title'],
            message="Subject with this title already exists",
        )]
