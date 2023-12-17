# Generated by Django 5.0 on 2023-12-16 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BootStrapAdmin', '0014_remove_rent_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='employee',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='BootStrapAdmin.employee'),
        ),
    ]
