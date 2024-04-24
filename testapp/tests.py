from django.test import TestCase
from django.urls import reverse
from testapp.models.Burger import BurgerModel as Burger
from datetime import datetime, timedelta

# Create your tests here.
class BurgerModelTest(TestCase):

    def setUp(self):
        Burger.objects.create(name="Test burger", price=100, weight=250, meat=Burger.Meat.VEGE, bacon=False, created=(datetime.now() - timedelta(minutes=4)))

    def test_values(self):
        burger = Burger.objects.get(name="Test burger")

        self.assertTrue(burger.price == 100)
        self.assertTrue(burger.weight == 250)
        self.assertTrue(burger.meat == Burger.Meat.VEGE)
        self.assertFalse(burger.bacon)


    def test_is_fresh(self):
        burger = Burger.objects.get(name="Test burger")

        self.assertTrue(burger.is_fresh())

    def test_is_eaten(self):
        burger = Burger.objects.get(name="Test burger")

        self.assertFalse(burger.is_eaten())
        burger.eat()
        self.assertTrue(burger.is_eaten())

    def test_is_vegan(self):
        burger = Burger.objects.get(name="Test burger")

        self.assertTrue(burger.is_vegan())

    def test_is_large(self):
        burger = Burger.objects.get(name="Test burger")

        self.assertTrue(burger.is_large())

    def test_is_expensive(self):
        burger = Burger.objects.get(name="Test burger")

        self.assertTrue(burger.is_expensive())

    def test_is_named(self):
        burger = Burger.objects.get(name="Test burger")

        self.assertTrue(burger.is_named())

    def test_creation_time(self):
        burger = Burger.objects.get(name="Test burger")

        self.assertTrue(burger.time_since_created() - timedelta(minutes=4) < timedelta(seconds=1))