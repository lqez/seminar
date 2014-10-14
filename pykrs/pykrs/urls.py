from django.conf.urls import patterns, include, url
from django.contrib import admin
from event.views import index

urlpatterns = patterns(
    '',
    url(r'^/?$', index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
)
