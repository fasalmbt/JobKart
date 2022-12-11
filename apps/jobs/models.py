from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=100, default='')
    desc = models.TextField()
    long_desc = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Apply(models.Model):
    job = models.ForeignKey(
        Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()
    created_by = models.ForeignKey(
        User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job) if self.job else ''

