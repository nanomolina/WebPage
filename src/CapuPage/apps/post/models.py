# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField
from apps.core.models import ProfilePerson
from apps.post import constants


class Author(models.Model):
    profile = models.ForeignKey(ProfilePerson, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.profile)


class Category(models.Model):
    number = models.IntegerField(max_length=3, choices=constants.CATEGORIES,
                                 unique=True)

    def __unicode__(self):
        return "%s" % (self.get_number_display())

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=250)
    authors = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='apps/post/static/post/img',
                              null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    content = HTMLField(null=True, blank=True)

    def image_url(self):
        if self.image != "":
          a, url = self.image.url.split('apps/post')
          response = url
        else:
          response = ""
        return response

    def __unicode__(self):
        return "%s" % (self.title)
