from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", null=True)
    title            = models.CharField(max_length=50,)
    description      = models.TextField(max_length=150, blank=True, null=True,)
    checked          = models.BooleanField(default=False,)
    creation_date    = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.text