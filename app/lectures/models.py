from django.conf import settings
from django.db import models
from subjects.models import Subject


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
