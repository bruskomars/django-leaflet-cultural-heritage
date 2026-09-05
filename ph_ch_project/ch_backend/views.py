from .models import Place, Category, City
from .serializers import CategorySerializer, PlaceSerializer, CitySerializer
from rest_framework import generics

from django.http import Http404
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import get_object_or_404

# Create your views here.
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'

class PlaceList(generics.ListAPIView):
    queryset = Place.objects.filter(active=True)
    serializer_class = PlaceSerializer
    name = 'place-list-active'

class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    name = 'place-detail'

class CityList(generics.ListAPIView):
    serializer_class = CitySerializer
    name = 'cities-list'

    def get_queryset(self):
        placeID = self.request.query_params.get('placeid', None)
        
        if placeID is None:
            raise Http404("Place ID is required.")
        
        selected_placeGeom = get_object_or_404(Place, pk=placeID).point_geometry
        nearest_cities = City.objects.annotate(distance=Distance('point_geometry', selected_placeGeom)).order_by('distance')[:3]
        
        return nearest_cities

#### OLD SERIALIZER
# def all_places(request):
#     queryset = Place.objects.all()
#     geojson = serialize('geojson', 
#                         queryset, 
#                         geometry_field='point_geometry', 
#                         srid=4326)
    
#     return HttpResponse(geojson, content_type='application/json')

# def place_detail(request, pk):
#     data = []
#     try:
#         place = Place.objects.get(pk=pk)
#         data.append(place)
#     except Place.DoesNotExist:
#         pass

#     geojson = serialize('geojson', data, geometry_field='point_geometry', srid=4326)
#     return HttpResponse(geojson, content_type='application/json')
