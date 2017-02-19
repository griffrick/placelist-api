from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^lists/(?P<list_key>[0-9]+)/$', views.PlacelistView.as_view()),
    url(r'^lists/$', views.PlacelistView.as_view()),
]