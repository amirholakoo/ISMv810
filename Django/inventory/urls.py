from django.urls import path
from . import views
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView  # Import other views as needed
from .views import (
    ShipmentListView, ShipmentCreateView, ShipmentUpdateView, ShipmentDeleteView,
    TruckListView, TruckCreateView, TruckUpdateView, TruckDeleteView,
    PurchaseListView, PurchaseCreateView, PurchaseUpdateView, PurchaseDeleteView,
)


urlpatterns = [
    path('', views.home, name='home'),
    # Add more paths as needed
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Shipment URLs
    path('shipments/', ShipmentListView.as_view(), name='shipment-list'),
    path('shipment/add/', ShipmentCreateView.as_view(), name='shipment-add'),
    path('shipment/<int:pk>/update/', ShipmentUpdateView.as_view(), name='shipment-update'),
    path('shipment/<int:pk>/delete/', ShipmentDeleteView.as_view(), name='shipment-delete'),
    # Truck URLs
    path('trucks/', TruckListView.as_view(), name='truck-list'),
    path('truck/add/', TruckCreateView.as_view(), name='truck-add'),
    path('truck/<int:pk>/update/', TruckUpdateView.as_view(), name='truck-update'),
    path('truck/<int:pk>/delete/', TruckDeleteView.as_view(), name='truck-delete'),
    # Purchase URLs
    path('purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('purchase/add/', PurchaseCreateView.as_view(), name='purchase-add'),
    path('purchase/<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase-update'),
    path('purchase/<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase-delete'),


]
