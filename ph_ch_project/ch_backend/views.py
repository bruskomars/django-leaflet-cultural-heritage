from .models import Place, Category, City
from .serializers import CategorySerializer, PlaceSerializer
from rest_framework import generics

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
