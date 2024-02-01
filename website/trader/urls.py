from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.home),
    path('aapl', views.aapl),
    path('low', views.low),
    path('mcd', views.mcd),

]