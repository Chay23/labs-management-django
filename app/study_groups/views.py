from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StudyGroup
from .serializers import StudyGroupSerializer


@permission_classes([IsAuthenticated])
class GroupsViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer


class GroupList(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        groups = StudyGroup.objects.all()
        serializer = StudyGroupSerializer(groups, many=True)
        return Response(serializer.data)
