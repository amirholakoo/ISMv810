from django.db import models

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    def __str__(self):
        return self.supplier_name

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    def __str__(self):
        return self.customer_name

class Truck(models.Model):
    license_number = models.CharField(max_length=255, unique=True)
    driver_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=[('Free', 'Free'), ('Busy', 'Busy')])
    location = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.license_number

class RawMaterial(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)

class Product(models.Model):
    reel_number = models.CharField(max_length=255, primary_key=True)
    width = models.IntegerField()
    gsm = models.IntegerField()
    length = models.IntegerField()
    grade = models.CharField(max_length=255, blank=True)
    breaks = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    qr_code = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[('In-stock', 'In-stock'), ('Sold', 'Sold'), ('Moved', 'Moved'), ('Delivered', 'Delivered')])
    receive_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField()

class Sale(models.Model):
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, blank=True, null=True)
    license_number = models.CharField(max_length=255, blank=True)
    list_of_reels = models.TextField()
    weight1 = models.DecimalField(max_digits=10, decimal_places=2)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.CharField(max_length=255, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_status = models.CharField(max_length=10, choices=[('Sent', 'Sent'), ('NA', 'NA')])
    payment_status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Unknown', 'Unknown'), ('Cancelled', 'Cancelled')])
    invoice_number = models.CharField(max_length=255, blank=True)
    document_info = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, blank=True, null=True, related_name='sale_shipment')

class Purchase(models.Model):
    date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, blank=True, null=True)
    material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    unit = models.CharField(max_length=10, choices=[('Bale', 'Bale'), ('Pallet', 'Pallet'), ('Bag', 'Bag'), ('Other', 'Other')])
    quantity = models.IntegerField()
    weight1 = models.DecimalField(max_digits=10, decimal_places=2)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.CharField(max_length=255, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_status = models.CharField(max_length=10, choices=[('Received', 'Received'), ('NA', 'NA')])
    payment_status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Unknown', 'Unknown'), ('Cancelled', 'Cancelled')])
    invoice_number = models.CharField(max_length=255, blank=True)
    document_info = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, blank=True, null=True, related_name='purchase_shipment')

class Shipment(models.Model):
    status = models.CharField(max_length=10, choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')])
    location = models.CharField(max_length=20, choices=[('Entrance', 'Entrance'), ('LoadingUnloading', 'LoadingUnloading'), ('LoadedUnloaded', 'LoadedUnloaded'), ('Office', 'Office'), ('Delivered', 'Delivered')])
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, blank=True, null=True)
    license_number = models.CharField(max_length=255, blank=True)
    entry_time = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    weight1 = models.DecimalField(max_digits=10, decimal_places=2)
    weight1_time = models.DateTimeField(blank=True, null=True)
    unload_location = models.CharField(max_length=255, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight2_time = models.DateTimeField(blank=True, null=True)
    list_of_reels = models.TextField(blank=True)
    sales = models.ForeignKey(Sale, on_delete=models.CASCADE, blank=True, null=True, related_name='shipment_sales')
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, blank=True, null=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, blank=True, null=True, related_name='shipment_purchase')
    vat = models.CharField(max_length=3, choices=[('YES', 'YES'), ('NO', 'NO')])
    invoice_status = models.CharField(max_length=10, choices=[('Sent', 'Sent'), ('Received', 'Received'), ('NA', 'NA')])
    payment_status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Unknown', 'Unknown'), ('Cancelled', 'Cancelled')])
    exit_time = models.DateTimeField(blank=True, null=True)
    document_info = models.TextField(blank=True)
    comments = models.TextField(blank=True)


class Consumption(models.Model):
    date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255, blank=True) # Consider removing if redundant with supplier FK
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.material_name} on {self.date}"


# Repeat the Anbar model structure for each Anbar table, adjusting the class name accordingly.

class AnbarGeneric(models.Model):
    receive_date = models.DateTimeField()
    reel_number = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255, blank=True) # Consider removing if redundant with supplier FK
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=[('In-stock', 'In-stock'), ('Moved', 'Moved'), ('Used', 'Used')])
    location = models.CharField(max_length=255)
    last_date = models.DateTimeField()
    width = models.IntegerField(blank=True, null=True)
    gsm = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True)
    breaks = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    qr_code = models.TextField(blank=True)

    class Meta:
        abstract = True # Make this model abstract so it's not created in the DB

class AnbarSangin(AnbarGeneric):
    pass

class AnbarSalonTolid(AnbarGeneric):
    pass

class AnbarAkhalKordan(AnbarGeneric):
    pass

class AnbarAkhalBiron(AnbarGeneric):
    pass

# Repeat for other Anbar types by defining similar classess

