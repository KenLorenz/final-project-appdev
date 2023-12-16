from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from BootStrapAdmin.models import *
from django.urls import reverse_lazy
from BootStrapAdmin.forms import *

# Create your views here.

# Customer CRUD

class CustomerView(ListView):
    model = Customer
    context_object_name = 'customer'
    template_name = ''
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CustomerCreate(CreateView):
    model = Customer
    form_class = ''
    template_name = '' # crud html
    success_url = reverse_lazy('')

class CustomerUpdate(UpdateView):
    model = Customer
    form_class = ''
    template_name = ''
    success_url = reverse_lazy('')
    
class CustomerDelete(DeleteView):
    model = Customer
    template_name = ''
    success_url = reverse_lazy('')
    
# Employee CRUD

class EmployeeView(ListView):
    model = Employee
    context_object_name = 'rent'
    template_name = ''
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EmployeeCreate(CreateView):
    model = Employee
    form_class = ''
    template_name = '' # crud html
    success_url = reverse_lazy('')

class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = ''
    template_name = ''
    success_url = reverse_lazy('')
    
class EmployeeDelete(DeleteView):
    model = Employee
    template_name = ''
    success_url = reverse_lazy('')
    
# Rents CRUD

class RentView(ListView):
    model = Rent
    context_object_name = 'rent'
    template_name = ''
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RentCreate(CreateView):
    model = Rent
    form_class = ''
    template_name = '' # crud html
    success_url = reverse_lazy('')

class RentUpdate(UpdateView):
    model = Rent
    form_class = ''
    template_name = ''
    success_url = reverse_lazy('')
    
class RentDelete(DeleteView):
    model = Rent
    template_name = ''
    success_url = reverse_lazy('')
    
# Model CRUD

class ModelView(ListView):
    model = Model
    context_object_name = 'model'
    template_name = ''
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ModelCreate(CreateView):
    model = Model
    form_class = ''
    template_name = '' # crud html
    success_url = reverse_lazy('')

class ModelUpdate(UpdateView):
    model = Model
    form_class = ''
    template_name = ''
    success_url = reverse_lazy('')
    
class ModelDelete(DeleteView):
    model = Model
    template_name = ''
    success_url = reverse_lazy('')
    
# Vehicle CRUD

class VehicleView(ListView):
    model = Vehicle
    context_object_name = 'vehicle'
    template_name = ''
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VehicleCreate(CreateView):
    model = Vehicle
    form_class = ''
    template_name = '' # crud html
    success_url = reverse_lazy('')

class VehicleUpdate(UpdateView):
    model = Vehicle
    form_class = ''
    template_name = ''
    success_url = reverse_lazy('')
    
class VehicleDelete(DeleteView):
    model = Vehicle
    template_name = ''
    success_url = reverse_lazy('')
    