from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save



# Create your models here.

class Place(models.Model):
	# Regular Django fields corresponding to the attributes in the
	# world borders shapefile.
	name = models.CharField(max_length=100)
	# Want this to be an array to support places which are bars and restaurants, etc
	place_type = models.CharField(max_length=50, null=True)

	city = models.CharField(max_length=100, null=True)
	neighborhood = models.CharField(max_length=100, null=True)
	street_address = models.CharField(max_length=100)
	url = models.CharField(max_length=200, null=True)
	photoUrl = models.CharField(max_length=200, null=True)

	state = models.CharField(max_length=100, null=True)
	zip_code = models.CharField(max_length=5, null=True)

	# list_count = models.IntegerField(default=0)

	lon = models.FloatField()
	lat = models.FloatField()

	# GeoDjango-specific: a geometry field (MultiPolygonField)
	# point = models.PointField()

	class Meta:
		ordering=('name', 'place_type', 'city', 'neighborhood', 'street_address', 'url', 'photoUrl', 'state', 'zip_code', 'lon', 'lat')

	# Returns the string representation of the model.
	def __unicode__(self):              # __unicode__ on Python 2
		return self.name

class Placelist(models.Model):

	title = models.CharField(max_length=100)
	author = models.ForeignKey(User, related_name='collaborators')
	collaborators = models.ManyToManyField(User, related_name='author', blank=True)
	list_type = models.CharField(max_length=25, null=True)
	#locations = models.ManyToManyField(City)
	# east_bound = models.FloatField()
	# west_bound = models.FloatField()
	# north_bound = models.FloatField()
	# south_bound = models.FloatField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now_add=True)
	followers = models.ManyToManyField(User, blank=True)
	places = models.ManyToManyField(Place, blank=True)

	class Meta:
		ordering=('title', 'author', 'list_type', 'created_on', 'updated_on')

	def __unicode__(self):              # __unicode__ on Python 2
		return self.title

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	city = models.CharField(max_length=25, null=True)
	registration_date = models.DateTimeField(auto_now_add=True)
	last_active = models.DateTimeField(auto_now_add=True)
	lists = models.ManyToManyField(Placelist, blank=True, related_name="subscriptions")
	subscriptions = models.ManyToManyField(Placelist, blank=True, related_name="lists")
	# 	collaborative_lists = models.ManyToManyField(Placelist, blank=True)
	starred_places = models.ManyToManyField(Place, blank=True)

	# followers = ManyToManyField(User)

	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)