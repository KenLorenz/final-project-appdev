# Generated by Django 5.0 on 2023-12-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BootStrapAdmin', '0019_model_model_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
