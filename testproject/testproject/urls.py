import os.path

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from testapp.views import index
from django.views.static import serve

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(.*)$', serve, kwargs={
            'document_root': settings.MEDIA_ROOT
        })
    ]
