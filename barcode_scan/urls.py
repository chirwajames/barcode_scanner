from django.contrib.auth import admin
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('home/', views.index, name="home")
]