from django.forms import ModelForm
from django import forms
from .models import *

class EmployeeForm(ModelForm):
    # birthdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Employee
        fields = "__all__"
        
class RentForm(ModelForm):
    # release_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Rent
        fields = "__all__"
        
class ModelForm(ModelForm):

    class Meta:
        model = Model
        fields = "__all__"
        
class VehicleForm(ModelForm):
    
    class Meta:
        model = Vehicle
        fields = "__all__"

class CustomerForm(ModelForm):
    
    class Meta:
        model = Customer
        fields = "__all__"