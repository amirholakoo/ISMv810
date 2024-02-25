from django.shortcuts import render
from .models import Supplier  # Import other models as needed

from django.urls import reverse_lazy
from .models import Product  # Add other models as needed
from .forms import ProductForm  # Add other forms as needed
from .models import Shipment, Truck, Purchase
from .forms import ShipmentForm, TruckForm, PurchaseForm


from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'inventory/home.html')
    # This view will use the 'home.html' template



# Product views

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'inventory/product_list.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

# Shipment Views
class ShipmentListView(ListView):
    model = Shipment
    context_object_name = 'shipments'
    template_name = 'inventory/shipment_list.html'

class ShipmentCreateView(CreateView):
    model = Shipment
    form_class = ShipmentForm
    template_name = 'inventory/shipment_form.html'
    success_url = reverse_lazy('shipment-list')

class ShipmentUpdateView(UpdateView):
    model = Shipment
    form_class = ShipmentForm
    template_name = 'inventory/shipment_form.html'
    success_url = reverse_lazy('shipment-list')

class ShipmentDeleteView(DeleteView):
    model = Shipment
    template_name = 'inventory/shipment_confirm_delete.html'
    success_url = reverse_lazy('shipment-list')

# Truck Views
class TruckListView(ListView):
    model = Truck
    context_object_name = 'trucks'
    template_name = 'inventory/truck_list.html'

class TruckCreateView(CreateView):
    model = Truck
    form_class = TruckForm
    template_name = 'inventory/truck_form.html'
    success_url = reverse_lazy('truck-list')

class TruckUpdateView(UpdateView):
    model = Truck
    form_class = TruckForm
    template_name = 'inventory/truck_form.html'
    success_url = reverse_lazy('truck-list')

class TruckDeleteView(DeleteView):
    model = Truck
    template_name = 'inventory/truck_confirm_delete.html'
    success_url = reverse_lazy('truck-list')

# Purchase Views
class PurchaseListView(ListView):
    model = Purchase
    context_object_name = 'purchases'
    template_name = 'inventory/purchase_list.html'

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/purchase_form.html'
    success_url = reverse_lazy('purchase-list')

class PurchaseUpdateView(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/purchase_form.html'
    success_url = reverse_lazy('purchase-list')

class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = 'inventory/purchase_confirm_delete.html'
    success_url = reverse_lazy('purchase-list')
