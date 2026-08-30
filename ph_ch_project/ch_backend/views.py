from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Place

# Create your views here.
def all_places(request):
    queryset = Place.objects.all()
    geojson = serialize('geojson', 
                        queryset, 
                        geometry_field='point_geometry', 
                        srid=4326)
    
    return HttpResponse(geojson, content_type='application/json')

def place_detail(request, pk):
    data = []
    try:
        place = Place.objects.get(pk=pk)
        data.append(place)
    except Place.DoesNotExist:
        pass

    geojson = serialize('geojson', data, geometry_field='point_geometry', srid=4326)
    return HttpResponse(geojson, content_type='application/json')
