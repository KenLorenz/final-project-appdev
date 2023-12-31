from typing import Any
from django.core.management.base import BaseCommand
from BootStrapAdmin.models import *
from faker import Faker
from random import randrange
from django.db import models
import datetime

class Command(BaseCommand):
    help = 'Creates dummy data for the application'

    def handle(self, *args, **kwargs):
        self.CreateRents()

    def CreateRents(self):
        fake = Faker()

        for _ in range(1, 10):
            STATUS_CHOICES = [
                'Ongoing',
                'Completed',
                'Cancelled',
            ]

            PAYMENT_CHOICES = [
                'Credit_Card',
                'Debit_Card',
                'Cash',
            ]

            status = fake.random_element(elements=STATUS_CHOICES)
            payment_type = fake.random_element(elements=PAYMENT_CHOICES)

            customer = Customer.objects.order_by('?').first()
            employee = Employee.objects.order_by('?').first()

            current_date = datetime.datetime.today()
            date_from = fake.date_time_between(start_date='-1y', end_date=current_date)
            date_to = fake.date_time_between(start_date=date_from, end_date=current_date)

            rent_instance = Rent.objects.create(
                status=status,
                payment_type=payment_type,
                employee=employee,
                customer=customer,
                date_from=date_from,
                date_to=date_to,
            )

            num_vehicles = fake.random_int(1, Vehicle.objects.count()) 
            vehicles = Vehicle.objects.order_by('?')[:num_vehicles]

            rent_instance.vehicle.set(vehicles)

            self.stdout.write(self.style.SUCCESS('Created a Rent row with vehicles.'))
