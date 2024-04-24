from django.db import models
from datetime import datetime
from datetime import timedelta
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import uuid


class BurgerModel(models.Model):
    class Meat(models.TextChoices):
        CHICKEN = "CH", _("Chicken")
        VEGE = "VG", _("Vegetarian")
        STEAK = "ST", _("Steak")
        FISH = "FI", _("Fish")

    name = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField(default=1)
    weight = models.PositiveSmallIntegerField(default=100)
    meat = models.CharField("Meat", max_length=2, choices=Meat, default=Meat.CHICKEN)
    bacon = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    pk = models.UUIDField(name="unique id", default=uuid.uuid4())
    eaten = False

    def __str__(self):
        return self.name

    def is_fresh(self):
        return self.time_since_created() <= timedelta(minutes=5)

    def is_eaten(self):
        return self.eaten

    def is_vegan(self):
        return self.meat == self.Meat.VEGE and not self.bacon

    def is_large(self):
        return self.weight > 200

    def is_expensive(self):
        return self.price > 25

    def is_named(self):
        return not (self.name == None or self.name == "")

    def time_since_created(self):
        return datetime.now().astimezone() - self.created

    def get_absolute_url(self):
        return reverse('burger-detail', kwargs={'pk': self.pk})

    def eat(self):
        self.eaten = True
        self.save()
