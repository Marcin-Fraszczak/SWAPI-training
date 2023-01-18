from django.db import models


class Page(models.Model):
    url = models.CharField(max_length=256)
    next = models.CharField(max_length=256, null=True, blank=True)
    previous = models.CharField(max_length=256, null=True, blank=True)
    filename = models.CharField(max_length=64)
