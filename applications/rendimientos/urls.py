from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path(
        'home/',
        views.Prueba.as_view(),
        name = 'home'
    ),
]