from rest_framework import serializers
from api.models import Placelist, Place

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('name', 'place_type', 'street_address', 'state', 'zip_code', 'lat', 'lon')

class PlacelistSerializer(serializers.ModelSerializer):
    # places = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='place-detail'
    # )
	class Meta:
		model = Placelist
		fields = ('title', 'author', 'collaborators', 'list_type', 'created_on', 'updated_on', 'followers', 'places')
		depth = 2