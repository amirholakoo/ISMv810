# Generated by Django 5.0.1 on 2024-02-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='receive_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
