# Generated by Django 5.0 on 2023-12-16 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BootStrapAdmin', '0010_alter_rent_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='employee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='BootStrapAdmin.employee'),
        ),
    ]