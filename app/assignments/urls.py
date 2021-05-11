from django.urls import path, include
from rest_framework import routers

from .views import AssignmentsBySubjectList, AssignmentViewSet

router = routers.DefaultRouter()
router.register("", AssignmentViewSet, basename='assignment')

urlpatterns = [
    path('', include(router.urls)),
    path('subject/<int:subject_id>/', AssignmentsBySubjectList.as_view(), name='assignments-by-subject-list')
]
