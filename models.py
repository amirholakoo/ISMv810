from django.db import models

class Truck(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    driver_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    STATUS_CHOICES = (
        ('incoming', 'Incoming'),
        ('loading', 'Loading'),
        ('unloaded', 'Unloaded'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='incoming')

    def __str__(self):
        return f"{self.license_plate} - {self.driver_name}"

class Shipment(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='shipments')
    shipment_date = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    )
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='created')

    def __str__(self):
        return f"Shipment {self.id} - {self.truck.license_plate}"

class PurchaseOrder(models.Model):
    shipment = models.OneToOneField(Shipment, on_delete=models.CASCADE, primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"PO {self.shipment.id}"
