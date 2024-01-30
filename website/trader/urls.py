from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.home),
    path('stne', views.stne),
    path('low', views.low),
    path('mcd', views.mcd),
]