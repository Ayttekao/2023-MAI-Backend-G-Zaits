"""carProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from lab_03.carProject.cardealer import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Cars
    path('api/cars', views.cars, name='cars'),
    path('api/cars/<int:car_id>', views.car_info, name='get_car_info'),

    # Customers
    path('api/customers', views.customers, name='customers'),
    path('api/customers/<int:customer_id>', views.customer_info, name='customer_info'),

    # Sales
    path('api/sales', views.sales, name='sales'),
    path('api/sales/<int:sale_id>', views.sale_info, name='sale_info'),
]
