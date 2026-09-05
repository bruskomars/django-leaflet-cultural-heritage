from .models import Category, Place, City
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PlaceSerializer(GeoFeatureModelSerializer):
    categories = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='category_name')
    class Meta:
        model = Place
        fields = (
            'pk',
            'categories',
            'place_name',
            'description',
            'created_at',
            'modified_at',
            'image',
        )
        geo_field = 'point_geometry'

class CitySerializer(GeoFeatureModelSerializer):
    proximity = serializers.SerializerMethodField('get_proximity')
    
    def get_proximity(self, obj):
        if obj.distance:
            return obj.distance.km
        else:
            return False
        
    class Meta:
        model = City
        fields = (
            'pk',
            'name',
            'proximity',
        )
        geo_field = 'point_geometry'