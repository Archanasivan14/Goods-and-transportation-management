# Generated by Django 5.0.7 on 2024-09-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0014_remove_order_tbl_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_tbl',
            name='orderstatus',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('Shipped', 'Shipped'), ('delivered', 'delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=30),
        ),
    ]
