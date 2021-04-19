from django.urls import path, include
from rest_framework import routers

from .views import AssignmentsBySubjectList, AssigmentViewSet

router = routers.DefaultRouter()

router.register("", AssigmentViewSet, basename='assignment')

urlpatterns = [
    path('', include(router.urls)),
    path('list/<str:subject>/', AssignmentsBySubjectList.as_view(), name='assignments-by-subject-list')
]
