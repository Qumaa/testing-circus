from django.shortcuts import render
from django.views.generic import DetailView

from .models import BurgerModel as Burger

# Create your views here.
class BurgerDetailView(DetailView):
    model = Burger
    template_name = 'testapp/burger_detail.html'
    context_object_name = 'burger'