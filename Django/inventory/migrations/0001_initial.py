# Generated by Django 5.0.1 on 2024-02-05 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('reel_number', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('width', models.IntegerField()),
                ('gsm', models.IntegerField()),
                ('length', models.IntegerField()),
                ('grade', models.CharField(blank=True, max_length=255)),
                ('breaks', models.CharField(blank=True, max_length=255)),
                ('comments', models.TextField(blank=True)),
                ('qr_code', models.TextField(blank=True)),
                ('location', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('In-stock', 'In-stock'), ('Sold', 'Sold'), ('Moved', 'Moved'), ('Delivered', 'Delivered')], max_length=10)),
                ('receive_date', models.DateTimeField()),
                ('last_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(max_length=255)),
                ('material_name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=255, unique=True)),
                ('driver_name', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('Free', 'Free'), ('Busy', 'Busy')], max_length=10)),
                ('location', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('unit', models.CharField(choices=[('Bale', 'Bale'), ('Pallet', 'Pallet'), ('Bag', 'Bag'), ('Other', 'Other')], max_length=10)),
                ('quantity', models.IntegerField()),
                ('weight1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_kg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vat', models.CharField(blank=True, max_length=255)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice_status', models.CharField(choices=[('Received', 'Received'), ('NA', 'NA')], max_length=10)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Unknown', 'Unknown'), ('Cancelled', 'Cancelled')], max_length=10)),
                ('invoice_number', models.CharField(blank=True, max_length=255)),
                ('document_info', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.rawmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('license_number', models.CharField(blank=True, max_length=255)),
                ('list_of_reels', models.TextField()),
                ('weight1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_kg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vat', models.CharField(blank=True, max_length=255)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice_status', models.CharField(choices=[('Sent', 'Sent'), ('NA', 'NA')], max_length=10)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Unknown', 'Unknown'), ('Cancelled', 'Cancelled')], max_length=10)),
                ('invoice_number', models.CharField(blank=True, max_length=255)),
                ('document_info', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], max_length=10)),
                ('location', models.CharField(choices=[('Entrance', 'Entrance'), ('LoadingUnloading', 'LoadingUnloading'), ('LoadedUnloaded', 'LoadedUnloaded'), ('Office', 'Office'), ('Delivered', 'Delivered')], max_length=20)),
                ('license_number', models.CharField(blank=True, max_length=255)),
                ('entry_time', models.DateTimeField()),
                ('weight1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight1_time', models.DateTimeField(blank=True, null=True)),
                ('unload_location', models.CharField(blank=True, max_length=255)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('weight2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('weight2_time', models.DateTimeField(blank=True, null=True)),
                ('list_of_reels', models.TextField(blank=True)),
                ('price_per_kg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shipping_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vat', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3)),
                ('invoice_status', models.CharField(choices=[('Sent', 'Sent'), ('Received', 'Received'), ('NA', 'NA')], max_length=10)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Unknown', 'Unknown'), ('Cancelled', 'Cancelled')], max_length=10)),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('document_info', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customer')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.rawmaterial')),
                ('purchase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipment_purchase', to='inventory.purchase')),
                ('sales', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipment_sales', to='inventory.sale')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
                ('truck', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.truck')),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='shipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_shipment', to='inventory.shipment'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='shipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_shipment', to='inventory.shipment'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier'),
        ),
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('supplier_name', models.CharField(blank=True, max_length=255)),
                ('material_type', models.CharField(max_length=255)),
                ('material_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(max_length=50)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='AnbarSangin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_date', models.DateTimeField()),
                ('reel_number', models.CharField(max_length=255)),
                ('supplier_name', models.CharField(blank=True, max_length=255)),
                ('material_type', models.CharField(max_length=255)),
                ('material_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('In-stock', 'In-stock'), ('Moved', 'Moved'), ('Used', 'Used')], max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('last_date', models.DateTimeField()),
                ('width', models.IntegerField(blank=True, null=True)),
                ('gsm', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=255)),
                ('breaks', models.CharField(blank=True, max_length=255)),
                ('comments', models.TextField(blank=True)),
                ('qr_code', models.TextField(blank=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnbarSalonTolid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_date', models.DateTimeField()),
                ('reel_number', models.CharField(max_length=255)),
                ('supplier_name', models.CharField(blank=True, max_length=255)),
                ('material_type', models.CharField(max_length=255)),
                ('material_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('In-stock', 'In-stock'), ('Moved', 'Moved'), ('Used', 'Used')], max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('last_date', models.DateTimeField()),
                ('width', models.IntegerField(blank=True, null=True)),
                ('gsm', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=255)),
                ('breaks', models.CharField(blank=True, max_length=255)),
                ('comments', models.TextField(blank=True)),
                ('qr_code', models.TextField(blank=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnbarAkhalKordan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_date', models.DateTimeField()),
                ('reel_number', models.CharField(max_length=255)),
                ('supplier_name', models.CharField(blank=True, max_length=255)),
                ('material_type', models.CharField(max_length=255)),
                ('material_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('In-stock', 'In-stock'), ('Moved', 'Moved'), ('Used', 'Used')], max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('last_date', models.DateTimeField()),
                ('width', models.IntegerField(blank=True, null=True)),
                ('gsm', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=255)),
                ('breaks', models.CharField(blank=True, max_length=255)),
                ('comments', models.TextField(blank=True)),
                ('qr_code', models.TextField(blank=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnbarAkhalBiron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_date', models.DateTimeField()),
                ('reel_number', models.CharField(max_length=255)),
                ('supplier_name', models.CharField(blank=True, max_length=255)),
                ('material_type', models.CharField(max_length=255)),
                ('material_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('In-stock', 'In-stock'), ('Moved', 'Moved'), ('Used', 'Used')], max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('last_date', models.DateTimeField()),
                ('width', models.IntegerField(blank=True, null=True)),
                ('gsm', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=255)),
                ('breaks', models.CharField(blank=True, max_length=255)),
                ('comments', models.TextField(blank=True)),
                ('qr_code', models.TextField(blank=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='sale',
            name='truck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.truck'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='truck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.truck'),
        ),
    ]
