from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from subjects.models import Subject

from .models import Lecture
from .serializers import LectureSerializer


@permission_classes([IsAuthenticated])
class LecturesBySubjectList(APIView):
    def get(self, request, *args, **kwargs):
        subject_id = kwargs.get("subject_id", "")
        lectures = Lecture.objects.filter(subject=subject_id)
        serializer = LectureSerializer(lectures, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
