from django.conf import settings
from django.db import models
from subjects.models import Subject


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
