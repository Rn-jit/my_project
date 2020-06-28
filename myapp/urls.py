from django.contrib import admin
from django.urls import path

from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('youtube', views.youtube, name='youtube'),
    path('chat/', views.chat, name='chat'),
    path('currency_exchange/', views.currency_convert, name='currency_exchange'),
    path('weather/', views.weather, name='weather')
]