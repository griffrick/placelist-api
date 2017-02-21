from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Place(models.Model):
	# Regular Django fields corresponding to the attributes in the
	# world borders shapefile.
	name = models.CharField(max_length=100)
	# Want this to be an array to support places which are bars and restaurants, etc
	place_type = models.CharField(max_length=50)

	# city = models.CharField(max_length=100)
	# neighborhood = models.CharField(max_length=100, null=True)
	street_address = models.CharField(max_length=100)
	# url = models.CharField(max_length=100, null=True)

	state = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=5, null=True)

	# list_count = models.IntegerField(default=0)

	lon = models.FloatField()
	lat = models.FloatField()

	# GeoDjango-specific: a geometry field (MultiPolygonField)
	# point = models.PointField()

	class Meta:
		ordering=('name', 'place_type', 'street_address', 'state', 'zip_code', 'lon', 'lat')

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

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)
	# location = models.ForeignKey(City)
	# followers = ManyToManyField(User)

	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username

