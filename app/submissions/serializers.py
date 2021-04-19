from rest_framework import serializers

from .models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"


class SubmissionSerializerUpdate(serializers.Serializer):
    attached_file = serializers.FileField(required=True)

    def update(self, instance, validated_data):
        instance.attached_file = validated_data.get('attached_file', instance.attached_file)
        instance.save()
        return instance
