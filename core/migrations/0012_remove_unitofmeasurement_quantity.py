# Generated by Django 5.0.6 on 2024-07-02 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_productimage_variant_alter_productimage_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitofmeasurement',
            name='quantity',
        ),
    ]
