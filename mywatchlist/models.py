from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.CharField(max_length=140, null=True)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.CharField(max_length=140, null=True)
    review = models.CharField(max_length=140, null=True)
