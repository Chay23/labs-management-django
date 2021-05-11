from django.urls import include, path
from rest_framework import routers

from .views import UsersViewSet, UserProfileViewSet, InstructorProfileViewSet, UserProfileByStudyGroup, \
    CreateUserView

router = routers.DefaultRouter()
router.register("users", UsersViewSet, basename="user")
router.register("profiles", UserProfileViewSet, basename="user-profile")
router.register("instructors", InstructorProfileViewSet, basename="instructor-profile")

urlpatterns = [
    path('', include(router.urls)),
    path('users/group/<int:group_id>/', UserProfileByStudyGroup.as_view(), name="user-group-list"),
    path('create-profile/', CreateUserView.as_view(), name="user-profile-create")
]
