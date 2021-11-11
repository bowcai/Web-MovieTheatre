from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)
    duration_min = models.PositiveSmallIntegerField()
    grade = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=8192)
    detail_url = models.CharField(max_length=8192)

    def __str__(self):
        return self.name
