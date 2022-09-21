from django.db import models

class MyWatchList(models.Model):
    title = models.CharField(max_length=140, null=True)
    watched = models.CharField(max_length=140, null=True)
    rating = models.CharField(max_length=140, null=True)
    release_date = models.CharField(max_length=140, null=True)
    review = models.CharField(max_length=140, null=True)
