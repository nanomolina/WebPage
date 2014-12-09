from django.conf.urls import patterns, include, url
from django.contrib import admin
from CapuPage import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('apps.core.urls', namespace='core')),
    url(r'^post/', include('apps.post.urls', namespace='post')),
)
