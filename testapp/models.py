from django.db import models


# Create your models here.
class ListCars(models.Model):
    carName = models.CharField(max_length=255)
    content = models.TextField(default='')
    price = models.PositiveSmallIntegerField(default=1)
    year = models.PositiveSmallIntegerField(default=2000)
    image = models.ImageField(upload_to='mediacar', blank=True, null=True)
