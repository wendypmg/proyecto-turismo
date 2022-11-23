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
from blog.views import *
from django.contrib.auth.views import LogoutView

app_name='blog'
urlpatterns = [
    path('', index, name='Home'),
#PRUEBA LIST VIEW DE DJANGO
    path('restaurantes', RestauranteListView.as_view(), name='Restaurante'),
    #path('restaurantes', views.restaurantes, name='Restaurante'),
    path('sitios', sitios, name='Sitio'),
    path('monumentos', monumentos, name='Monumento'),

    path('formHTML', form_html),
    path('restaurante-django-forms', restaurante_forms_django, name='RestaurantesDjangoForms'),
    path('sitio-django-forms', sitio_forms_django, name='SitiosDjangoForms'),
    path('monumento-django-forms', monumento_forms_django, name='MonumentosDjangoForms'),

    #path('search', search, name='Search'),

#RESTAURANTE
    path('restaurante/<int:pk>/update', update_restaurante, name='UpdateRestaurante'),
    path('restaurante/<int:pk>/delete', delete_restaurante, name='DeleteRestaurante'),

    path('restaurante/add/', RestauranteCreateView.as_view(), name='restaurante-add'),
    path('restaurante/<int:pk>/detail', RestauranteDetailView.as_view(), name='restaurante-detail'),
    path('restaurante/<int:pk>/update', RestauranteUpdateView.as_view(), name='restaurante-update'),
    path('restaurante/<int:pk>/delete', RestauranteDeleteView.as_view(), name='restaurante-delete'),

    path('restaurantes/', RestauranteListView.as_view(), name='restaurante-list'),

#MONUMENTO
    path('monumento/<int:pk>/update', update_monumento, name='UpdateMonumento'),
    path('monumento/<int:pk>/delete', delete_monumento, name='DeleteMonumento'),

    path('monumento/add/', MonumentoCreateView.as_view(), name='monumento-add'),
    path('monumento/<int:pk>/detail', MonumentoDetailView.as_view(), name='monumento-detail'),
    path('monumento/<int:pk>/update', MonumentoUpdateView.as_view(), name='monumento-update'),
    path('monumento/<int:pk>/delete', MonumentoDeleteView.as_view(), name='monumento-delete'),

    path('monumentos/', MonumentoListView.as_view(), name='monumento-list'),

#SITIO
    path('sitio/<int:pk>/update', update_sitio, name='UpdateSitio'),
    path('sitio/<int:pk>/delete', delete_sitio, name='DeleteSitio'),

    path('sitio/add/', SitioCreateView.as_view(), name='sitio-add'),
    path('sitio/<int:pk>/detail', SitioDetailView.as_view(), name='sitio-detail'),
    path('sitio/<int:pk>/update', SitioUpdateView.as_view(), name='sitio-update'),
    path('sitio/<int:pk>/delete', SitioDeleteView.as_view(), name='sitio-delete'),

    path('sitios/', SitioListView.as_view(), name='sitio-list'),

#LOGIN
    path('login/', login_request, name="Login"),

#REGISTRO
    path('register/', register, name='user-register'),
    path('register/update', user_update, name='user-update'),
    path('avatar/load', avatar_load, name='avatar-load'),

#LOGOUT
    path('logout/', logout_request, name="Logout"),

 ]


