import os
import time

from assignments.models import Assignment
from django.conf import settings
from django.db import models
from labs_management.storage import OverwriteStorage
from users.models import UserProfile


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    profile = UserProfile.objects.get(user=instance.created_by.id)
    filename = "%s_%s_%s_%s.%s" % (profile.group, profile.first_name, profile.last_name, instance.assignment.title, ext)
    return os.path.join("labs/%s/%s" % (time.strftime("%Y"), profile.group), filename)


class Submission(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.DO_NOTHING)
    attached_file = models.FileField(storage=OverwriteStorage, upload_to=content_file_name)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return self.assignment.title
