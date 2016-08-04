from django.db import models

class Urls(models.Model):
    short = models.CharField(max_length=50)
    long = models.CharField(max_length=4000)
    status = models.CharField(max_length=3)
    title = models.CharField(max_length=256)
