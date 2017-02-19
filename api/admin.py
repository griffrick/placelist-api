from django.contrib import admin
from api.models import Placelist, Place, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Placelist)
admin.site.register(Place)