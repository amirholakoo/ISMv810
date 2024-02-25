from django import forms
from .models import Supplier, Product, Truck, Customer, Sale, Purchase, Shipment

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = '__all__'
