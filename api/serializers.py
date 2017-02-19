from rest_framework import serializers
from api.models import Placelist

class PlacelistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Placelist
		fields = ('title', 'author', 'collaborators', 'list_type', 'created_on', 'updated_on', 'followers', 'places')