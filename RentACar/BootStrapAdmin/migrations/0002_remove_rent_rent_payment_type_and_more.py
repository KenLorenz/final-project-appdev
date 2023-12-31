# Generated by Django 5.0 on 2023-12-16 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BootStrapAdmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='rent_payment_type',
        ),
        migrations.RemoveField(
            model_name='rentstatus',
            name='rent_code',
        ),
        migrations.RemoveField(
            model_name='rentstatus',
            name='rent_description',
        ),
        migrations.AddField(
            model_name='rent',
            name='payment_type',
            field=models.CharField(choices=[('Credit Card Payment', 'Credit'), ('Debit Card Payment', 'Debit'), ('Cash Payment', 'Cash')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='PaymentType',
        ),
    ]
