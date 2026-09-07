from django.shortcuts import render

# Create your views here.
def placesListMap(request):
    return render(request, 'ch_frontend/places_list_map.html')