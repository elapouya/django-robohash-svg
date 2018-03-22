#
# Created : 2018-02-16
#
# @author: Eric Lapouyade
#

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from .views import *

urlpatterns = [
    path('', IndexView.as_view(),
         name='index'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)