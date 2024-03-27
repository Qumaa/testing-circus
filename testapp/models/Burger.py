from django.db import models
from datetime import datetime
from datetime import timedelta
from django.urls import reverse


class BurgerModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField(default=1)
    weight = models.PositiveSmallIntegerField(default=100)
    meat = models.TextChoices("Meat", "CHIKCKEN VEGE STEAK FISH")
    bacon = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    pk = models.IntegerField(name="unique id")
    eaten = False

    def __str__(self):
        return self.name

    def is_fresh(self):
        return (datetime.now().date() - self.created) <= timedelta(minutes=5)

    def get_absolute_url(self):
        return reverse('burger-detail', kwargs={'pk': self.pk})

    def eat(self):
        self.eaten = True
        self.save()