from django.contrib import admin
from .models import PointsOrder, Att456, Riverdata, datepicker, Userlocation, Shop, Hotpoints
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
admin.site.register(PointsOrder, LeafletGeoAdmin)
admin.site.register(Att456, LeafletGeoAdmin)
admin.site.register(Riverdata, LeafletGeoAdmin)
admin.site.register(datepicker)
admin.site.register(Userlocation)
admin.site.register(Hotpoints, LeafletGeoAdmin)


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')