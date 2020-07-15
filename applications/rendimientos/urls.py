from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path(
        'region',
        views.region,
        name = 'region'
    ),
    path(
        '',
        views.home,
        name = 'home'
    ),
    path(
        'asistencias',
        views.asistencias,
        name = 'asistencias'
    ),
]
