from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from subjects.models import Subject

from .models import Assignment
from .serializers import AssignmentSerializer


@permission_classes([IsAuthenticated])
class AssignmentsBySubjectList(APIView):
    def get(self, request, *args, **kwargs):
        subject_id = kwargs.get("subject_id", "")
        assignments = Assignment.objects.filter(subject=subject_id)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
