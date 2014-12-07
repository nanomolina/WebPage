from django.db import models
from tinymce.models import HTMLField
from apps.core.models import ProfilePerson


class Author(models.Model):
    profile = models.ForeignKey(ProfilePerson, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.profile)

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ManyToManyField(Author)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.ImageField(upload_to='apps/post/static/post/img', null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    content = HTMLField(null=True, blank=True)

    def image_url(self):
        a, url = self.image.url.split('apps/post')
        return url

    def __unicode__(self):
        return "%s" % (self.title)
