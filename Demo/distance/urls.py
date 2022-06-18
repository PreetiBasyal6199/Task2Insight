from django.urls import path,include
from .views import CalculateView
urlpatterns = [
    path('', CalculateView),
]