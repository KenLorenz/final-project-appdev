from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from BootStrapAdmin.models import *
from django.urls import reverse_lazy
from BootStrapAdmin.forms import *
from django.shortcuts import render

def IndexView(request):
    return render(request, 'Index.html')

# Create your views here.

# Customer CRUD

class CustomerView(ListView):
    model = Customer
    context_object_name = 'customer'
    template_name = 'customers.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CustomerCreate(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'crud/add.html' # crud html
    success_url = reverse_lazy('customer-view')

class CustomerUpdate(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'crud/update.html'
    success_url = reverse_lazy('customer-view')
    
class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'crud/delete.html'
    url = reverse_lazy('customer-delete')
    success_url = reverse_lazy('customer-view')
    
# Employee CRUD

class EmployeeView(ListView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employees.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'crud/add.html' # crud html
    success_url = reverse_lazy('employee-view')

class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'crud/update.html'
    success_url = reverse_lazy('employee-view')
    
class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'crud/delete.html'
    url = reverse_lazy('employee-delete')
    success_url = reverse_lazy('employee-view')
    
# Rents CRUD

class RentView(ListView):
    model = Rent
    context_object_name = 'rent'
    template_name = 'rents.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RentCreate(CreateView):
    model = Rent
    form_class = RentForm
    template_name = 'crud/add.html' # crud html
    success_url = reverse_lazy('rent-view')

class RentUpdate(UpdateView):
    model = Rent
    form_class = RentForm
    template_name = 'crud/update.html'
    success_url = reverse_lazy('rent-view')
    
class RentDelete(DeleteView):
    model = Rent
    template_name = 'crud/delete.html'
    url = reverse_lazy('rent-delete')
    success_url = reverse_lazy('rent-view')
    
# Model CRUD

class ModelView(ListView):
    model = Model
    context_object_name = 'model'
    template_name = 'models.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ModelCreate(CreateView):
    model = Model
    form_class = modelForm
    template_name = 'crud/add.html' # crud html
    success_url = reverse_lazy('model-view')

class ModelUpdate(UpdateView):
    model = Model
    form_class = modelForm
    template_name = 'crud/update.html'
    success_url = reverse_lazy('model-view')
    
class ModelDelete(DeleteView):
    model = Model
    template_name = 'crud/delete.html'
    url = reverse_lazy('rent-delete')
    success_url = reverse_lazy('rent-view')
    
# Vehicle CRUD

class VehicleView(ListView):
    model = Vehicle
    context_object_name = 'vehicle'
    template_name = 'vehicles.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VehicleCreate(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'crud/add.html' # crud html
    success_url = reverse_lazy('vehicle-view')

class VehicleUpdate(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'crud/update.html'
    success_url = reverse_lazy('vehicle-view')
    
class VehicleDelete(DeleteView):
    model = Vehicle
    template_name = 'crud/delete.html'
    url = reverse_lazy('vehicle-delete')
    success_url = reverse_lazy('vehicle-view')
    