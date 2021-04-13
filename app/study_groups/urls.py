from django.urls import include, path
from rest_framework import routers

from .views import GroupsViewSet

router = routers.DefaultRouter()
router.register("", GroupsViewSet, basename="group")

urlpatterns = [
    path('', include(router.urls)),
]
