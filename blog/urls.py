"""turismo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.test import TestCase

from django.urls import path
from blog import views

app_name='blog'
urlpatterns = [
    path('', views.index, name='Home'),
    path('restaurantes', views.restaurantes, name='Estudios'),
    path('sitios', views.sitios, name='Viajes'),
    path('monumentos', views.monumentos, name='Empleos'),

    path('formHTML', views.form_hmtl),
    path('restaurante-django-forms', views.restaurante_forms_django, name='RestauranteDjangoForms'),
    path('sitio-django-forms', views.sitio_forms_django, name='SitioDjangoForms'),
    path('monumento-django-forms', views.monumento_forms_django, name='MonumentoDjangoForms'),

    path('search', views.search, name='Search'),

#RESTAURANTE
    path('restaurante/<int:pk>/update', views.update_restaurante, name='UpdateRestaurante'),
    path('restaurante/<int:pk>/delete', views.delete_restaurante, name='DeleteRestaurante'),

    path('restaurante/add/', views.RestauranteCreateView.as_view(), name='restaurante-add'),
    path('restaurante/<int:pk>/detail', views.RestauranteDetailView.as_view(), name='restaurante-detail'),
    path('restaurante/<int:pk>/update', views.RestauranteUpdateView.as_view(), name='restaurante-update'),
    path('restaurante/<int:pk>/delete', views.RestauranteDeleteView.as_view(), name='restaurante-delete'),

    path('restaurantes', views.RestauranteListView.as_view(), name='restaurante-list'),

#MONUMENTO
    path('monumento/<int:pk>/update', views.update_monumento, name='UpdateMonumento'),
    path('monumento/<int:pk>/delete', views.delete_monumento, name='DeleteMonumento'),

    path('monumento/add/', views.MonumentoCreateView.as_view(), name='monumento-add'),
    path('monumento/<int:pk>/detail', views.MonumentoDetailView.as_view(), name='monumento-detail'),
    path('monumento/<int:pk>/update', views.MonumentoUpdateView.as_view(), name='monumento-update'),
    path('monumento/<int:pk>/delete', views.MonumentoDeleteView.as_view(), name='monumento-delete'),

    path('monumentos', views.MonumentoListView.as_view(), name='monumento-list'),

#SITIO
    path('sitio/<int:pk>/update', views.update_sitio, name='UpdateViaje'),
    path('sitio/<int:pk>/delete', views.delete_sitio, name='DeleteViaje'),

    path('sitio/add/', views.SitioCreateView.as_view(), name='sitio-add'),
    path('sitio/<int:pk>/detail', views.SitioDetailView.as_view(), name='sitio-detail'),
    path('sitio/<int:pk>/update', views.SitioUpdateView.as_view(), name='sitio-update'),
    path('sitio/<int:pk>/delete', views.SitioDeleteView.as_view(), name='sitio-delete'),

    path('sitios', views.SitioListView.as_view(), name='sitio-list'),
]


