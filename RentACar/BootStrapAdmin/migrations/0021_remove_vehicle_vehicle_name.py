# Generated by Django 5.0 on 2023-12-16 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BootStrapAdmin', '0020_vehicle_vehicle_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_name',
        ),
    ]
