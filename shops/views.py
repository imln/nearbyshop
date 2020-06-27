from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.http import HttpResponse
from django.core import serializers

longitude = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)


def ShopList(request):
	model = Shop
	context_object_name = 'shops'
	queryset = Shop.objects.annotate(distance=Distance('location',user_location)).order_by('distance')[0:6]
	post_list = serializers.serialize('json', queryset)
	return HttpResponse(post_list, content_type="text/json-comment-filtered")
    