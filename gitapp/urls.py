
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index,name=""),
    path("login", views.login,name="login"),
]
