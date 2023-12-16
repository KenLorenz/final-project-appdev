from django.db import models

# Create your models here.

# Assuming Philippine Localized business, and renting multiple cars in one name is also allowed

# related commands: makemigrations, migrate

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Customer(BaseModel): # Related to Rent Table
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    
    gender = models.CharField(max_length = 10, null=False, choices=GENDER_CHOICES)
    
    email_address = models.CharField(max_length = 100, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False)
    
    street = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.first_name, self.last_name # Might not work ): (two returns)
    

class Model(BaseModel): # Related to Vehicle Table
    model_code = models.CharField(max_length=100, null=False, blank=False)
    model_name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.model_name

class Vehicle(BaseModel): # Related to Rent Table
    model = models.OneToOneField(Model, blank=True, null=True, on_delete=models.CASCADE)
    engine_size = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.model

class RentStatus(BaseModel): # Related to Rent Table
    STATUS_CHOICES = (
        ('Ongoing','Ongoing'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    )
    
    rent_code = models.CharField(max_length=100, null=False, blank=False)
    
    rent_status = models.CharField(max_length=50, null=False, choices=STATUS_CHOICES)
    
    rent_description= models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.rent_status

class PaymentType(BaseModel): # Related to Rent Table
    PAYMENT_CHOICES = (
        ('Credit Card Payment','Credit'),
        ('Debit Card Payment','Debit'),
        ('Cash Payment','Cash'),
    )
    
    payment_type = models.CharField(max_length=100, null=False, choices=PAYMENT_CHOICES)
    
    def __str__ (self):
        return self.payment_type

class Rent(BaseModel):
    status = models.ForeignKey(RentStatus, blank=False, on_delete=models.CASCADE)
    
    customer = models.ManyToManyField(Customer)
    
    rent_payment_type = models.ForeignKey(PaymentType, null=False, blank=False, on_delete=models.CASCADE)
    
    vehicle = models.ManyToManyField(Vehicle)
    
    date_from = models.DateField(null=False, blank=False)
    date_to = models.DateField(null=False, blank=False)
    