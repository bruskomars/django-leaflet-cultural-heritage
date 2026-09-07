from django.urls import path
from . import views

app_name = 'ch_frontend'
urlpatterns = [
    path('', views.placesListMap, name='places_list_map'),
] 