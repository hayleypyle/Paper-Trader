from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index),
    path('aapl', views.aapl, name='apple'),
    path('msft', views.msft, name='microsoft'),
    path('goog', views.goog, name='google'),
    
]