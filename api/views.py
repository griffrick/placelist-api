from rest_framework.response import Response
from api.models import Placelist, Place, UserProfile
from api.serializers import PlacelistSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

class PlacelistView(APIView):

	def get_many_lists(self):
		lists = Placelist.objects.all().order_by('-updated_on')
		serializer = PlacelistSerializer(lists, many=True)
		return Response(serializer.data)

	def get_one_list(self, list_key):
		num_list = Placelist.objects.get(id = list_key)
		serializer = PlacelistSerializer(num_list)
		return Response(serializer.data) 

	def get(self, request, list_key='0'):
		print "list key is " + list_key
		if(list_key is '0'):
			return self.get_many_lists()
		else:
			return self.get_one_list(list_key)

	def post(self, request):
		print(request.data)
		serializer = PlacelistSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		

	#     else:
	#         serializer = QuerySerializer(data=request.data)
	#         if serializer.is_valid():
	#             return Response(serializer.data, status=status.HTTP_201_CREATED)
	#         else:
	#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# def delete(self, request):
	#     qid = request.data['id']
	#     u = Query.objects.get(id=qid)
	#     u.saved = False
	#     u.save()
	#     serializer = QuerySerializer(data=request.data)
	#     if serializer.is_valid():
	#         return Response(serializer.data, status=status.HTTP_201_CREATED)
	#     else:
	#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)