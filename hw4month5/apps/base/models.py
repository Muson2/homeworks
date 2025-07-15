from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
