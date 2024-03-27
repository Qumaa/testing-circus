from django.contrib import admin

from testapp.models import BurgerModel
from testapp.models.CarModel import ListCars

# Register your models here.
admin.site.register(ListCars)
admin.site.register(BurgerModel)
