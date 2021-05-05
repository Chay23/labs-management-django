from django.urls import include, path
from rest_framework import routers

from .views import SubjectViewSet, SubjectsByGroupList, SubjectsByUserList

router = routers.DefaultRouter()
router.register("", SubjectViewSet, basename="subject")

urlpatterns = [
    path('user-group/list', SubjectsByGroupList.as_view(), name="subjects-by-group-list"),
    path('user/list', SubjectsByUserList    .as_view(), name="subjects-by-instructor-list"),
    path('', include(router.urls))
]
