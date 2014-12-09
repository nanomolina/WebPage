from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, null=True ,blank=True)
    modified = models.DateTimeField(auto_now=True, null=True ,blank=True)

    def __unicode__(self):
        return "%s" % (self.name,)


class ProfilePerson(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    group = models.ManyToManyField(Group)
    created = models.DateTimeField(auto_now_add=True, null=True ,blank=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class SlideImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    show_name = models.BooleanField(default=True)
    image = models.ImageField(upload_to='apps/core/static/core/img/slides',
                              null=True, blank=True)
    show_image = models.BooleanField(default=True)

    def image_url(self):
        if self.image != "":
          a, url = self.image.url.split('apps/core')
          response = url
        else:
          response = ""
        return response

    def __unicode__(self):
        return "%s" % (self.name,)


class Slide(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30)
    images = models.ManyToManyField(SlideImage)
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = Slide.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except Slide.DoesNotExist:
                pass
        super(Slide, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % (self.name,)
