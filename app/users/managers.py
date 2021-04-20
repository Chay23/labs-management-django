from django.contrib.auth.models import BaseUserManager, User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email


class UserManager(BaseUserManager):
    def create_with_profile(self, email: str, password: str, first_name: str, last_name: str, group_id: int):
        from .models import UserProfile
        from study_groups.models import StudyGroup
        """
        Creates, saves and return a User with appropriate UserProfile
        :param email:
        :param password:
        :return:
        """
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_student = True
        user.save(using=self._db)

        group = StudyGroup.objects.get(id=group_id)

        profile = UserProfile(
            user=user,
            first_name=first_name,
            last_name=last_name,
            group=group
        )
        profile.save()
        return user

    def create_user(self, email: str, password: str = None) -> User:
        """
        Creates, saves and returns a User.
        Args:
            email: email field value
            password: password field value
        Returns:
            new User instance
        """
        if not email:
            raise ValueError("Users must have an email address")

        validate_email(email)
        validate_password(password)

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str = None) -> User:
        """
        Same as create_user(), but sets is_instructor and is_superuser to True.
        Args:
            email: email field value
            password: password field value
        Returns:
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
