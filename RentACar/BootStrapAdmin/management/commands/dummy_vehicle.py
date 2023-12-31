from typing import Any
from django.core.management.base import BaseCommand
from BootStrapAdmin.models import *
from faker import Faker
from random import randrange
from django.db import models
import os
from pathlib import Path


class Command(BaseCommand):
    help = 'Creates dummy data for the application'
    
    def handle(self, *args, **kwargs) -> str | None:
        self.CreateCars()
            
    def CreateCars(self): # does not include images
        fake = Faker()
        
        for x in range(1,10):

            engine_size = fake.random_int(100,1000)
            
            existing_ids = Model.objects.values_list('id')
            
            try:
                model = Model(id=existing_ids[fake.random_int(0,len(existing_ids[0]))][0])
            except:
                model = None
            
            preview = os.path.join('images_test', f'{fake.random_int(1,5)}.jpg')
             
            row = Vehicle(engine_size=engine_size,
                        model=model, preview=preview)
            
            row.save()
            self.stdout.write(self.style.SUCCESS('Created a Car row.'))
        