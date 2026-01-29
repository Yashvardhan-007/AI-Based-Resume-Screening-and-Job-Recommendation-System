from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
