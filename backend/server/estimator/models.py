from django.db import models

# Create your models here.

class Housing(models.Model):
    zipcode = models.IntegerField()
    surface = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    floors = models.IntegerField()
    waterfront = models.IntegerField()
    condition = models.IntegerField()
    bathbed_ratio = models.FloatField()
    estimation = models.IntegerField()