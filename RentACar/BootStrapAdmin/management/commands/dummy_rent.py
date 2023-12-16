from typing import Any
from django.core.management.base import BaseCommand
from BootStrapAdmin.models import *
from faker import Faker
from random import randrange
from django.db import models
import datetime



class Command(BaseCommand):
    help = 'Creates dummy data for the application'
    
    def handle(self, *args, **kwargs) -> str | None:
        self.CreateRents()
    
    def CreateRents(self):
        fake = Faker()
        
        for x in range(1,10):
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
            
            status = STATUS_CHOICES[fake.random_int(0,2)]
            
            payment_type = PAYMENT_CHOICES[fake.random_int(0,2)]
            
            
            customer_ids = Customer.objects.values_list('id')
            
            employee_ids = Employee.objects.values_list('id')
            

            employee = Employee(id=employee_ids[fake.random_int(0,len(employee_ids[0]))][0])
            
            customer = Customer(id=customer_ids[fake.random_int(0,len(customer_ids[0]))][0])


            current_date = datetime.datetime.today()
            date_from = fake.date_time_between(start_date='-1y', end_date=current_date)
            date_to = fake.date_time_between(start_date=date_from, end_date=current_date)
            
            row = Rent(status=status,payment_type=payment_type,
                       employee=employee,customer=customer,
                       date_from=date_from,date_to=date_to)
            row.save()
            
            
            vehicle = Vehicle.objects.values_list('id')
            
            temp = []
            
            for x in range(0,fake.random_int(0,len(vehicle))): # randomizes length of cars per rent as well as randomizes the car id
                temp.append(vehicle[fake.random_int(0,len(vehicle)-1)][0])
                
            row.vehicle.set(temp)
            
                
            
            self.stdout.write(self.style.SUCCESS('Created an Rent row.'))
        
        