from django.contrib.gis import admin
from .models import Category, Place, City

# Register your models here.
admin.site.register(Category)

class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 14,
            'default_lon': 121.037281,
            'default_lat': 14.569973,
        }
    }


@admin.register(Place)
class PlaceAdmin(CustomGeoAdmin):
    pass

@admin.register(City)
class CityAdmin(CustomGeoAdmin):
    pass