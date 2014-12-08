from django.conf.urls import patterns, include, url
from apps.post.views import blogPost, blogCategory

urlpatterns = patterns(
    '',
    url(r'^(?P<post_id>\d+)/$', blogPost, name='blog-post'),
    url(r'^category/(?P<category_num>\d+)/$', blogCategory,
        name='blog-category'),
)
