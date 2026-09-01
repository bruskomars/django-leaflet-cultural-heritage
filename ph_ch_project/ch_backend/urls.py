from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name=views.CategoryList.name)
    # path('places/', views.all_places, name='all_places'),
    # path('places/<int:pk>', views.place_detail, name='place_detail'),
] 
