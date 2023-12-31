"""
URL configuration for RentACar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from BootStrapAdmin.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', IndexView, name='index'),
    
    path('customer_view', CustomerView.as_view(), name='customer-view'),
    path('customer_view/add', CustomerCreate.as_view(), name='customer-add'),
    path('customer_view/<pk>', CustomerUpdate.as_view(), name='customer-update'),
    path('customer_view/<pk>/delete', CustomerDelete.as_view(), name='customer-delete'),
    
    path('employee_view', EmployeeView.as_view(), name='employee-view'),
    path('employee_view/add', EmployeeCreate.as_view(), name='employee-add'),
    path('employee_view/<pk>', EmployeeUpdate.as_view(), name='employee-update'),
    path('employee_view/<pk>/delete', EmployeeDelete.as_view(), name='employee-delete'),
    
    path('vehicle_view', VehicleView.as_view(), name='vehicle-view'),
    path('vehicle_view/add', VehicleCreate.as_view(), name='vehicle-add'),
    path('vehicle_view/<pk>', VehicleUpdate.as_view(), name='vehicle-update'),
    path('vehicle_view/<pk>/delete', VehicleDelete.as_view(), name='vehicle-delete'),
    
    path('model_view', ModelView.as_view(), name='model-view'),
    path('model_view/add', ModelCreate.as_view(), name='model-add'),
    path('model_view/<pk>', ModelUpdate.as_view(), name='model-update'),
    path('model_view/<pk>/delete', ModelDelete.as_view(), name='model-delete'),
    
    path('rent_view', RentView.as_view(), name='rent-view'),
    path('rent_view/add', RentCreate.as_view(), name='rent-add'),
    path('rent_view/<pk>', RentUpdate.as_view(), name='rent-update'),
    path('rent_view/<pk>/delete', RentDelete.as_view(), name='rent-delete'),
    
    #path('images_test/')
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
