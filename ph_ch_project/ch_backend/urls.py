from django.urls import path
from . import views

urlpatterns = [
    path('places/', views.all_places, name='all_places'),
    path('places/<int:pk>', views.place_detail, name='place_detail'),
] 
