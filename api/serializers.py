from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Placelist, Place, UserProfile


class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place

		fields = ('id','name', 'place_type', 'city', 'neighborhood', 'street_address', 'url', 'photoUrl', 'state', 'zip_code', 'lon', 'lat')

class PlacelistSerializerGet(serializers.ModelSerializer):
    # places = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='place-detail'
    # )
	class Meta:
		model = Placelist
		fields = ('id','title', 'author', 'collaborators', 'list_type', 'created_on', 'updated_on', 'followers', 'places')
		depth = 2

class PlacelistSerializer(serializers.ModelSerializer):
    # places = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='place-detail'
    # )
	class Meta:
		model = Placelist
		fields = ('id','title', 'author', 'collaborators', 'list_type', 'created_on', 'updated_on', 'followers', 'places')


class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer(required=True)
	class Meta:
		model = User
		fields = '__all__'

class UserSerializer2(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','email','date_joined','profile')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','user','city', 'registration_date', 'last_active', 'lists', 'subscriptions', 'starred_places')
        depth = 2





