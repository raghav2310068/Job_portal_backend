from django.db import models
from accounts.models import Users


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
