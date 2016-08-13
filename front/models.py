from django.db import models

class Urls(models.Model):
    title = models.CharField(max_length=256)
    short = models.CharField(max_length=50)
    long = models.CharField(max_length=4000)
    wayback = models.CharField(max_length=4000)
    timestamp = models.CharField(max_length=16)
    status = models.CharField(max_length=3)
