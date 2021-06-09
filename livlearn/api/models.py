from django.db import models


class Test(models.Model):
    stuff = models.CharField(blank=True, max_length=500, default='')
