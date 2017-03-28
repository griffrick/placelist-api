from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api import views

urlpatterns = [

    url(r'^lists/(?P<list_key>[0-9]+)/$', views.PlacelistView.as_view()),
    url(r'^lists/(?P<list_key>[0-9]+)/places/(?P<place_key>[0-9]+)/$', views.PlacelistView.as_view()),
    url(r'^lists/$', views.PlacelistView.as_view()),
    url(r'places/$', views.Place.as_view()),
    url(r'places/(?P<place_key>[0-9]+)/$', views.Place.as_view()),
    url(r'places/pending/$', views.PendingPlaces.as_view()),
    url(r'^login/', obtain_jwt_token),
    url(r'^register/', views.Register.as_view()),
    url(r'^users/$', views.UsersView.as_view()),
    url(r'users/(?P<user_key>[0-9]+)/$', views.UserProfileView.as_view()),
    url(r'^users/profile/$', views.UsersProfilesView.as_view()),
    url(r'^token-refresh/', refresh_jwt_token),
]