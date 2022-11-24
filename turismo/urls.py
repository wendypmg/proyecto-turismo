from django.contrib import admin
from django.urls import path, include
from blog.views import *
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='Home'),
    path('blog/', include('blog.urls')),
    path('home/', include('home.urls')),
]
