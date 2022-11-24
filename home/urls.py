
from django.contrib import admin
from django.urls import path, include
from blog.views import *
from home.views import *

app_name='home'
urlpatterns = [
            path('', home, name='main'),
            path('Angelica', AboutAngelicaView, name='about-Angelica'),
            path('Wendy', AboutWendyView, name='about-Wendy'),
            path('Sofia', AboutSofiaView, name='about-Sofia'),

]