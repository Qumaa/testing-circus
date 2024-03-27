from django.urls import path
from .views import BurgerDetailView

urlpatterns = [
    path('burger/<int:pk>/', BurgerDetailView.as_view(), name='burger-detail')
]
