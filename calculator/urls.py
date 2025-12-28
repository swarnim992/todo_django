from django.urls import path

from .views import calculator_home

urlpatterns = [
    path('', calculator_home, name='calculator_home'),
]
