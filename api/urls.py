from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api import views

urlpatterns = [

    url(r'^lists/(?P<list_key>[0-9]+)/$', views.PlacelistView.as_view()),
    url(r'^lists/$', views.PlacelistView.as_view()),

    url(r'places/$', views.Place.as_view()),
    url(r'places/(?P<place_key>[0-9]+)/$', views.Place.as_view()),

    url(r'register/$', views.Register.as_view()),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),

]