from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s" % (self.name,)


class ProfilePerson(models.Model):
	first_name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30)
	group = models.ManyToManyField(Group)

	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name)