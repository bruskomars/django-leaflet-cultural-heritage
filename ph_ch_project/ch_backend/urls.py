from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name=views.CategoryList.name),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name=views.CategoryDetail.name),
    path('places/', views.PlaceList.as_view(), name=views.PlaceList.name),
    path('places/<int:pk>/', views.PlaceDetail.as_view(), name=views.PlaceDetail.name),
    path('cities/', views.CityList.as_view(), name=views.CityList.name),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('places/', views.all_places, name='all_places'),
    # path('places/<int:pk>', views.place_detail, name='place_detail'),
] 

urlpatterns = format_suffix_patterns(urlpatterns)