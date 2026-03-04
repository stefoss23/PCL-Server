from django.urls import path
from . import views

urlpatterns = [
    path('simple/', views.simple, name='simple'),
    path('primes/', views.primes, name='primes'),
    path('sfault', views.sfault, name='sfault'),
    path('ex1', views.ex1, name='ex1'),
    path('ex2', views.ex2, name='ex2'),
    path('memloss', views.memloss, name='memloss')
]
