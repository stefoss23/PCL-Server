from django.urls import path
from . import views

urlpatterns = [
    path('number/', views.number, name='number'),
    path('primes/', views.primes, name='primes'),
    path('sfault', views.sfault, name='sfault'),
    path('ex1', views.ex1, name='ex1')
]
