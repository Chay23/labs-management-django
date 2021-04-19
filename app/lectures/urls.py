from django.urls import path, include
from rest_framework import routers

from .views import LectureViewSet, LecturesBySubjectList

router = routers.DefaultRouter()

router.register("", LectureViewSet, basename='lecture')

urlpatterns = [
    path('', include(router.urls)),
    path('list/<str:subject>/', LecturesBySubjectList.as_view(), name='lectures-by-subject-list')
]
