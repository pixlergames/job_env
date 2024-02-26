from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Job(models.Model):
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='jobs')
    # Add other fields related to the job

    def __str__(self):
        return self.title