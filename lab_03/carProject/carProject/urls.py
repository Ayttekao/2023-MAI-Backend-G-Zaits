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
from django.urls import path, include
from cardealer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('healthcheck/', views.HealthCheckView.as_view(), name='healthcheck'),
    path('cars/', views.CarsView.as_view(), name='cars'),
    path('cars/<int:id>/', views.CarInfoView.as_view(), name='car_info'),
    path('cars/search/', views.CarSearchView.as_view(), name='car_search'),
    path('customers/', views.CustomersView.as_view(), name='customers'),
    path('customers/<int:id>/', views.CustomerInfoView.as_view(), name='customer_info'),
    path('sales/', views.SalesView.as_view(), name='sales'),
    path('sales/<int:id>/', views.SaleInfoView.as_view(), name='sale_info'),
]
