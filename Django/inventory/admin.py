from django.contrib import admin
from .models import Supplier, Customer, Truck, RawMaterial, Product, Sale, Purchase, Shipment  # Add other models as needed
from .models import AnbarSangin, AnbarSalonTolid,AnbarAkhalKordan,AnbarAkhalBiron, Consumption


admin.site.register(Supplier)
admin.site.register(Customer)

admin.site.register(RawMaterial)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Purchase)

admin.site.register(Consumption)

admin.site.register(AnbarSangin)
admin.site.register(AnbarSalonTolid)
admin.site.register(AnbarAkhalKordan)
admin.site.register(AnbarAkhalBiron)



# If you need to customize the admin for a specific model, use the following pattern:

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'location')  # Customize with fields you want to display
    list_filter = ('status', 'location')
    search_fields = ('status', 'location')

# Repeat the pattern for other models
admin.site.register(Shipment, ShipmentAdmin)

# Example for custom admin for Truck
class TruckAdmin(admin.ModelAdmin):
    list_display = ('license_number', 'driver_name', 'status')
    list_filter = ('status',)
    search_fields = ('license_number', 'driver_name')

admin.site.register(Truck, TruckAdmin)
