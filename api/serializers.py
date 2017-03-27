from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Placelist, Place


class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('id', 'name', 'photoUrl', 'place_type', 'street_address', 'state', 'zip_code', 'lat', 'lon')

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
	class Meta:
		model = User
		fields = '__all__'

		# class UserSerializer(serializers.ModelSerializer):
		# 	class Meta:
		# 		model = User
		# 		city = serializers.CharField(source='UserProfile.city')
		# 		registration_date = serializers.DateTimeField(source='UserProfile.registration_date')
		# 		last_active = serializers.DateTimeField(source='UserProfile.last_active')

		# 		lists = serializers.ManyRelatedField(source='UserProfile.lists')
		# 		subscriptions = serializers.ManyRelatedField(source='UserProfile.subscriptions')
		# 		collaborative_lists = serializers.ManyRelatedField(source='UserProfile.collaborative_lists')
		# 		starred_places = serializers.ManyRelatedField(source='UserProfile.starred_places')

		# 		fields = ('id', 'username', 'password', 'email')

		# 	write_only_fields = ('password',)
		# 	read_only_fields = ('id',)


		# def create(self, validated_data):
		# 	user = User.objects.create(
		# 		username=validated_data['username'],
		# 		email=validated_data['email']
		# 	)

		# 	user.set_password(validated_data['password'])
		# 	user.save()

		# 	return user


		# class AppUserSerializer(serializers.ModelSerializer):
		# 	username = serializers.CharField(source='user.username')
		# 	email = serializers.CharField(source='user.email')
		# 	password = serializers.CharField(source='user.password')
		# 	city = serializers.CharField(source='UserProfile.city')
		# 	registration_date = serializers.DateTimeField(source='registration_date')
		# 	last_active = serializers.DateTimeField(source='last_active')

		# 	lists = serializers.ManyRelatedField(source='lists')
		# 	subscriptions = serializers.ManyRelatedField(source='subscriptions')
		# 	collaborative_lists = serializers.ManyRelatedField(source='collaborative_lists')
		# 	starred_places = serializers.ManyRelatedField(source='starred_places')

		# 	class Meta:
		# 		model = UserProfile
		# 		fields = (
		# 			'id', 'username', 'email', 'password', 'city', 'registration_date', 'last_active', 'lists', 'subscriptions',
		# 			'collaborative_lists', 'starred_places')

		# 	def restore_object(self, attrs, instance=None):
		# 		"""
		# 		Given a dictionary of deserialized field values, either update
		# 		an existing model instance, or create a new model instance.
		# 		"""
		# 		if instance is not None:
		# 			instance.user.email = attrs.get('user.email', instance.user.email)
		# 			instance.user.password = attrs.get('user.password', instance.user.password)
		# 			instance.city = attrs.get('city', instance.city)
		# 			instance.registration_date = attrs.get('registration_date', instance.registration_date)
		# 			instance.last_active = attrs.get('last_active', instance.last_active)
		# 			instance.lists = attrs.get('lists', instance.lists)
		# 			instance.subscriptions = attrs.get('subscriptions', instance.subscriptions)
		# 			instance.collaborative_lists = attrs.get('collaborative_lists', instance.collaborative_lists)
		# 			instance.starred_places = attrs.get('starred_places', instance.starred_places)

		# 			return instance

		# 		user = User.objects.create_user(username=attrs.get('user.username'), email=attrs.get('user.email'),
		# 										password=attrs.get('user.password'))
		# 		return UserProfile(user=user)
