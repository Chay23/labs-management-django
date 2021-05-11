from django.urls import path, include
from rest_framework import routers

from .views import SubmissionViewSet, SubmissionsByAssignmentList, FileDownloadAPIView, SubmissionByUserId

router = routers.DefaultRouter()
router.register("", SubmissionViewSet, basename="submission")

urlpatterns = [
    path("", include(router.urls)),
    path("assignment/<int:assignment_id>/", SubmissionsByAssignmentList.as_view(),
         name="submissions-by-assignment-list"),
    path("file/<str:filename>/", FileDownloadAPIView.as_view(), name="submission-file",
         ),
    path("assignment/<int:assignment_id>/user/<int:user_id>/", SubmissionByUserId.as_view(),
         name="submission-by-user-id")
]
