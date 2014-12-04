from django.conf.urls import patterns, include, url
from apps.core.views import home

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
)
