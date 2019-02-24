from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings

from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.home.view_home, name='view_config_home'),
]

# Adiconando parametros para carregar imagens no template
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
