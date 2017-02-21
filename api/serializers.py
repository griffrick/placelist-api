from rest_framework import serializers
from api.models import Placelist, Place

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('name', 'place_type', 'street_address', 'state', 'zip_code', 'lat', 'lon')

class PlacelistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Placelist
		fields = ('title', 'author', 'collaborators', 'list_type', 'created_on', 'updated_on', 'followers', 'places')