# Generated by Django 5.0 on 2023-12-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BootStrapAdmin', '0018_rent_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='model_type',
            field=models.CharField(default=None, max_length=100),
        ),
    ]