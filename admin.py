from django.contrib import admin
from .models import Truck, Shipment, PurchaseOrder

admin.site.register(Truck)
admin.site.register(Shipment)
admin.site.register(PurchaseOrder)
