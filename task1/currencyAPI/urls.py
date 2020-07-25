# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('result', views.getMinimums),
]