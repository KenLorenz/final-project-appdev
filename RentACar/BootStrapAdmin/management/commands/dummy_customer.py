from typing import Any
from django.core.management.base import BaseCommand
from BootStrapAdmin.models import *
from faker import Faker
from random import randrange
from django.db import models




class Command(BaseCommand):
    help = 'Creates dummy data for the application'
    
    def handle(self, *args, **kwargs) -> str | None:
        self.CreateCustomers()
    
    def CreateCustomers(self):
        fake = Faker()
        
        for x in range(1,18):
            rnd_name = fake.name()
            rnd_name = rnd_name.split()
            
            first_name = rnd_name[0]
            last_name = rnd_name[1]
            
            email = fake.email()
            phone_num = fake.phone_number()
            
            middle_name = fake.name()
            middle_name = middle_name.split()[1]
            
            street = fake.street_address()
            city = fake.city()
            row = Customer(first_name=first_name,middle_name=middle_name,last_name=last_name,
                        email_address=email,phone_number=phone_num,street=street,city=city)
            
            row.save()
            self.stdout.write(self.style.SUCCESS('Created a Customer row.'))
        
        