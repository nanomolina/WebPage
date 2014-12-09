from django.conf.urls import patterns, include, url
from apps.core.views import home, login, logout

urlpatterns = patterns(
    '',
    url(r'^$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
)
