from typing import Any
from django.core.management.base import BaseCommand
from BootStrapAdmin.models import *
from faker import Faker
from random import randrange
from django.db import models




class Command(BaseCommand):
    help = 'Creates dummy data for the application'
    
    def handle(self, *args, **kwargs) -> str | None:
        self.CreateModels()
        self.CreateCars()
    
    def CreateModels(self):
        fake = Faker()
        
        for x in range(1,10):
            
            model_code = fake.bothify(text='???###')
            company = fake.company()
            row = Model(model_code=model_code,company=company)
            
            row.save()
            self.stdout.write(self.style.SUCCESS('Created a Model row.'))
            
    def CreateCars(self): # does not include images
        fake = Faker()
        
        for x in range(1,10):

            engine_size = fake.random_int(100,1000)
            
            existing_ids = Model.objects.values_list('id')
            
            try:
                model = Model(id=existing_ids[fake.random_int(0,len(existing_ids[0]))][0])
            except:
                model = None
            
            
            row = Vehicle(engine_size=engine_size,
                        model=model)
            
            row.save()
            self.stdout.write(self.style.SUCCESS('Created a Car row.'))
        