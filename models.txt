Complete Models Definition
Below are the Django model definitions for your database schema. These models include the entities for Trucks, Suppliers, Raw Materials, Products, Customers, Sales, Purchases, Shipments, Anbars, and Consumption, reflecting the relationships and data types specified in your SQL schema.

Customers Model
python
Copy code
class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=255)
    comments = models.TextField()
Suppliers Model
python
Copy code
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=255)
    comments = models.TextField()
Trucks Model
python
Copy code
class Truck(models.Model):
    STATUS_CHOICES = [
        ('Free', 'Free'),
        ('Busy', 'Busy'),
    ]
    license_number = models.CharField(max_length=255, unique=True)
    driver_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    location = models.CharField(max_length=255)
RawMaterials Model
python
Copy code
class RawMaterial(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    comments = models.TextField()
Products Model
python
Copy code
class Product(models.Model):
    STATUS_CHOICES = [
        ('In-stock', 'In-stock'),
        ('Sold', 'Sold'),
        ('Moved', 'Moved'),
        ('Delivered', 'Delivered'),
    ]
    reel_number = models.CharField(max_length=255, primary_key=True)
    width = models.IntegerField()
    gsm = models.IntegerField()
    length = models.IntegerField()
    grade = models.CharField(max_length=255)
    breaks = models.CharField(max_length=255)
    comments = models.TextField()
    qr_code = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    receive_date = models.DateTimeField()
    last_date = models.DateTimeField()
Sales Model
python
Copy code
class Sale(models.Model):
    INVOICE_STATUS_CHOICES = [
        ('Sent', 'Sent'),
        ('NA', 'NA'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Terms', 'Terms'),
        ('Unknown', 'Unknown'),
        ('Cancelled', 'Cancelled'),
    ]
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True, blank=True)
    license_number = models.CharField(max_length=255)
    list_of_reels = models.TextField()
    weight1 = models.DecimalField(max_digits=10, decimal_places=2)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_status = models.CharField(max_length=4, choices=INVOICE_STATUS_CHOICES)
    payment_status = models.CharField(max_length=9, choices=PAYMENT_STATUS_CHOICES)
    invoice_number = models.CharField(max_length=255)
    document_info = models.TextField()
    comments = models.TextField()
    # shipment = models.ForeignKey('Shipment', on_delete=models.SET_NULL, null=True, blank=True)  # Uncomment if needed
Purchases Model
python
Copy code
class Purchase(models.Model):
    INVOICE_STATUS_CHOICES = [
        ('Received', 'Received'),
        ('NA', 'NA'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Terms', 'Terms'),
        ('Unknown', 'Unknown'),
        ('Cancelled', 'Cancelled'),
    ]
    date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True, blank=True)
    material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, null=True, blank=True)
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    quantity = models.IntegerField()
    weight1 = models.DecimalField(max_digits=10, decimal_places=2)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_status = models.CharField(max_length=9, choices=INVOICE_STATUS_CHOICES)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
    invoice_number = models.CharField(max_length=255)
    document_info = models.TextField()
    comments = models.TextField()
    # shipment = models.ForeignKey('Shipment', on_delete=models.SET_NULL, null=True, blank=True)  # Uncomment if needed
Shipments Model
python
Copy code
class Shipment(models.Model):
    STATUS_CHOICES = [
        ('Incoming', 'Incoming'),
        ('Outgoing', 'Outgoing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    LOCATION_CHOICES = [
        ('Entrance', 'Entrance'),
        ('LoadingUnloading', 'LoadingUnloading'),
        ('LoadedUnloaded', 'LoadedUnloaded'),
        ('Office', 'Office'),
        ('Delivered', 'Delivered'),
    ]
    INVOICE_STATUS_CHOICES = [
        ('Sent', 'Sent'),
        ('Received', 'Received'),
        ('NA', 'NA'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Terms', 'Terms'),
        ('Unknown', 'Unknown'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=16, choices=LOCATION_CHOICES)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=255)
    entry_time = models.DateTimeField()
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    weight1 = models.DecimalField(max_digits=10, decimal_places=2)
    weight1_time = models.DateTimeField()
    unload_location = models.CharField(max_length=255)
    quantity = models.IntegerField()
    weight2 = models.DecimalField(max_digits=10, decimal_places=2)
    weight2_time = models.DateTimeField()
    list_of_reels = models.TextField()
    sales = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True, blank=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, null=True, blank=True)
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True, blank=True)
    vat = models.CharField(max_length=3, choices=[('YES', 'Yes'), ('NO', 'No')])
    invoice_status = models.CharField(max_length=9, choices=INVOICE_STATUS_CHOICES)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
    exit_time = models.DateTimeField()
    document_info = models.TextField()
    comments = models.TextField()
Anbar Model
The Anbar model you provided suggests that you have multiple specific types of Anbars (e.g., Anbar_Sangin, Anbar_Salon_Tolid). To simplify this and make it more flexible, we can create a single Anbar model with a type field to differentiate between them, as previously suggested. However, if your business logic significantly differs between these Anbar types, maintaining separate models as you've defined might be necessary.

For brevity, I'll show how to define a generic Anbar model, and you can replicate this approach or adjust it according to your specific requirements for each Anbar type.

python
Copy code
class Anbar(models.Model):
    STATUS_CHOICES = [
        ('In-stock', 'In-stock'),
        ('Moved', 'Moved'),
        ('Used', 'Used'),
    ]
    anbar_type = models.CharField(max_length=255)  # To distinguish between different Anbars
    receive_date = models.DateTimeField()
    reel_number = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255)
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    location = models.CharField(max_length=255)
    last_date = models.DateTimeField()
    width = models.IntegerField()
    gsm = models.IntegerField()
    length = models.IntegerField()
    grade = models.CharField(max_length=255)
    breaks = models.CharField(max_length=255)
    comments = models.TextField()
    qr_code = models.TextField()
Consumption Model
python
Copy code
class Consumption(models.Model):
    date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255)
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
Implementation Notes
Relationships: I've included ForeignKey relationships where specified. Remember that Django automatically handles the creation of primary keys (ID fields), so you don't need to define them explicitly for each model.
Choices: For fields with a limited set of options (like statuses), I've used Django's choices feature. This ensures that only valid options can be stored in these fields.
Nullable Relationships: In cases where a relationship might not always be present (e.g., a Sale might not always have a related Shipment initially), I've used null=True, blank=True in the ForeignKey definition. Adjust these based on your business logic.
Modularization: If your application grows large, consider splitting your models into separate modules (files) within your app for better maintainability.