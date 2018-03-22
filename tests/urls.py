#
# Created : 2018-03-22
#
# @author: Eric Lapouyade
#

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django_robohash.views import robohash
from .views import *

urlpatterns = [
    path('', IndexView.as_view(),
         name='index'),
    path('robohash/<string>/', robohash,
         name='robohash')
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)