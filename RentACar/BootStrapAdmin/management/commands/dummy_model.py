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
    
    def CreateModels(self):
        fake = Faker()
        
        for x in range(1,10):
            
            model_code = fake.bothify(text='???###')
            company = fake.company()
            row = Model(model_code=model_code,company=company)
            
            row.save()
            self.stdout.write(self.style.SUCCESS('Created a Model row.'))
        