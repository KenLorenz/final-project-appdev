# Generated by Django 5.0 on 2023-12-16 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BootStrapAdmin', '0021_remove_vehicle_vehicle_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='model_name',
            new_name='company',
        ),
    ]