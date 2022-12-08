from django.contrib import admin
from django.urls import path, include
from blog.views import *
from home.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='Home'),
    path('blog/', include('blog.urls')),
    path('home/', include('home.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)