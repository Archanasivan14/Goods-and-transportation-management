# Generated by Django 3.0.7 on 2024-08-21 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_vehicle_tbl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle_tbl',
            old_name='vn',
            new_name='vnm',
        ),
    ]
