from django.urls import include, path
from rest_framework import routers

from .views import SubjectsList, SubjectViewSet

router = routers.DefaultRouter()
router.register("", SubjectViewSet, basename="subject")

urlpatterns = [
    path('list/by_group', SubjectsList.as_view(), name="subjects-by-group-list"),
    path('', include(router.urls))
]
