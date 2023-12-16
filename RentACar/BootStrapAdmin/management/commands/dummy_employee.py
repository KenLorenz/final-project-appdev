from typing import Any
from django.core.management.base import BaseCommand
from BootStrapAdmin.models import *
from faker import Faker
from random import randrange
from django.db import models




class Command(BaseCommand):
    help = 'Creates dummy data for the application'
    
    def handle(self, *args, **kwargs) -> str | None:
        self.CreateEmployees()
    
    def CreateEmployees(self):
        fake = Faker()
        
        for x in range(1,10):
            rnd_name = fake.name()
            rnd_name = rnd_name.split()
            
            first_name = rnd_name[0]
            last_name = rnd_name[1]
            
            email = fake.email()
            phone_num = fake.phone_number()
            
            middle_name = fake.name()
            middle_name = middle_name.split()[1]
            
            privilege = randrange(1,4) # 1 to 3
            
            existing_ids = Employee.objects.values_list('id')
            
            try:
                in_charge = Employee(id=existing_ids[fake.random_int(0,len(existing_ids[0]))][0])
            except:
                in_charge = None
                
            row = Employee(first_name=first_name,middle_name=middle_name,last_name=last_name,
                        email_address=email,phone_number=phone_num,privilege=privilege,
                        in_charge=in_charge)
            
            row.save()
            self.stdout.write(self.style.SUCCESS('Created an Employee row.'))
        
        