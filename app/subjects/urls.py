from django.urls import include, path
from rest_framework import routers

from .views import SubjectsList, SubjectViewSet

router = routers.DefaultRouter()
router.register("", SubjectViewSet, basename="user")

urlpatterns = [
    path('group/list', SubjectsList.as_view(), name="subject-list"),
    path('', include(router.urls))
]
