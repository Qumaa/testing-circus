from django.test import TestCase
from django.urls import reverse
from testapp.models.Burger import BurgerModel as Burger
from datetime import datetime, timedelta

# Create your tests here.
class BurgerModelTest(TestCase):

    def setUp(self) -> None:
        Burger.objects.create(name="Test burger", price=100, weight=250, meat="Fish", bacon=False, created=(datetime.now() - timedelta(minutes=6)), pk=-1)

    def test_is_fresh(self):
        burger = Burger.objects.get(name="Test burger")

        self.assertTrue(not burger.is_fresh())
