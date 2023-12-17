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
        
class Employee(BaseModel): # Related to Rent Table
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    
    email_address = models.CharField(max_length = 100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    
    privilege = models.IntegerField(default=1, null=False, blank=False)
    
    in_charge = models.ForeignKey('self', null=True, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        if (self.middle_name == None):
            m_name = ""
        else:
            m_name = self.middle_name
        return f'{self.first_name} {m_name} {self.last_name}'

class Customer(BaseModel): # Related to Rent Table
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    
    gender = models.CharField(max_length = 100, null=False, blank=False, choices=GENDER_CHOICES)
    
    email_address = models.CharField(max_length = 100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    
    street = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        if (self.middle_name == None):
            m_name = ""
        else:
            m_name = self.middle_name
        return f'{self.first_name} {m_name} {self.last_name}'
    

class Model(BaseModel): # Related to Vehicle Table
    model_code = models.CharField(max_length=100, null=False, blank=False)
    company = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.model_code

class Vehicle(BaseModel): # Related to Rent Table
    model = models.ForeignKey(Model, blank=True, null=True, on_delete=models.CASCADE)
    engine_size = models.IntegerField(null=False, blank=False,default=0)
    
    # FIX THIS LATER
    preview = models.ImageField(upload_to='images_test', null=True)
    
    def __str__(self):
        return str(self.model)

class Rent(BaseModel):
    STATUS_CHOICES = (
        ('Ongoing','Ongoing'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    )
    
    PAYMENT_CHOICES = (
        ('Credit Card Payment','Credit_Card'),
        ('Debit Card Payment','Debit_Card'),
        ('Cash Payment','Cash'),
    )
    
    status = models.CharField(max_length=100, null=False, choices=STATUS_CHOICES)
    
    customer = models.ForeignKey(Customer, default="", blank=False, on_delete=models.CASCADE)
    
    employee = models.ForeignKey(Employee, default=0, null=True, blank=True, on_delete=models.CASCADE)
    
    payment_type = models.CharField(max_length=100, null=False, choices=PAYMENT_CHOICES)
    
    vehicle = models.ManyToManyField(Vehicle) # FIX LATER
    
    date_from = models.DateField(null=False, blank=False)
    date_to = models.DateField(null=False, blank=False)
    
    def __str__(self):
        return str(self.customer)