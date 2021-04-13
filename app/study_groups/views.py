from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import StudyGroup
from .serializers import StudyGroupSerializer


@permission_classes([IsAuthenticated])
class GroupsViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
