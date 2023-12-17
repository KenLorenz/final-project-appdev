from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Model)

class ModelAdmin(admin.ModelAdmin):
    list_display = ('company','model_code','created_at','updated_at')
    search_fields = ('company',)

@admin.register(Vehicle)

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('model','engine_size','preview')
    search_fields = ('model',)
    
@admin.register(Rent)

class RentAdmin(admin.ModelAdmin):
    list_display = ('customer','payment_type','status','date_from','date_to')
    search_fields = ('customer',)
    
    def get_vehicles(self, obj):
        return ", ".join([vehicle.name for vehicle in obj.vehicle.all()])
    
@admin.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','middle_name','last_name','gender','email_address',
                    'phone_number','street','city','created_at','updated_at')
    search_fields = ('first_name',)
    
@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','middle_name','last_name','email_address',
                    'phone_number','privilege','in_charge','created_at','updated_at')
    search_fields = ('first_name',)