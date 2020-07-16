from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
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
    path(
        'rendimientos',
        views.rendimientos,
        name = 'rendimientos'
    ),
    path(
        'rendimientos-cursos',
        views.cursos,
        name = 'rendimientos-cursos'
    ),
    path(
        'idps',
        views.idps,
        name = 'idps'
    ),
]
