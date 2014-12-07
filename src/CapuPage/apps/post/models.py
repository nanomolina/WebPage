from django.db import models
from apps.core.models import ProfilePerson


class Author(models.Model):
    profile = models.ForeignKey(ProfilePerson, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    # date_first_post = models.DateTimeField(auto_now_add=True)
    # date_last_post = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.profile)

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ManyToManyField(Author)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='apps/post/static/post/img', null=True)
    subtitle = models.CharField(max_length=250, blank=True)
    text = models.TextField()

    def __unicode__(self):
        return "%s" % (self.title)
