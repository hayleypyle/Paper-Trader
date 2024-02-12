from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index),
    path('aapl', views.aapl),
    path('msft', views.msft),
    path('goog', views.goog),
    
]