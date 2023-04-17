from django.http import JsonResponse
from django.views import View

from cardealer.models import Car, Customer, Make, Sale
import json


class CarsView(View):
    def get(self, request):
        cars = Car.objects.all()
        data = [
            {
                'id': car.id,
                'make': {
                    'id': car.make.id,
                    'name': car.make.name
                },
                'model': car.model,
                'year': car.year,
                'price': car.price
            } for car in cars]
        return JsonResponse(data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        make_name = data.get('make')
        model = data.get('model')
        year = data.get('year')
        price = data.get('price')
        try:
            make = Make.objects.get(name=make_name)
            car = Car.objects.create(make=make, model=model, year=year, price=price)
            data = {
                'id': car.id,
                'make': car.make.name,
                'model': car.model,
                'year': car.year,
                'price': car.price
            }
            return JsonResponse(data)
        except Make.DoesNotExist:
            return JsonResponse({'error': f'Make with name {make_name} does not exist'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CarInfoView(View):
    def get(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
            data = {
                'id': car.id,
                'make': {
                    'id': car.make.id,
                    'name': car.make.name
                },
                'model': car.model,
                'year': car.year,
                'price': car.price
            }
            return JsonResponse(data)
        except Car.DoesNotExist:
            return JsonResponse({'error': f'Car with id {car_id} does not exist'}, status=404)

    def put(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
            data = json.loads(request.body)
            make_name = data.get('make')
            model = data.get('model')
            year = data.get('year')
            price = data.get('price')
            make = Make.objects.get(name=make_name)

            car.make = make
            car.model = model
            car.year = year
            car.price = price
            car.save()

            data = {
                'id': car.id,
                'make': {
                    'id': car.make.id,
                    'name': car.make.name
                },
                'model': car.model,
                'year': car.year,
                'price': car.price
            }
            return JsonResponse(data)
        except Car.DoesNotExist:
            return JsonResponse({'error': f'Car with id {car_id} does not exist'}, status=404)

    def delete(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            return JsonResponse({'message': f'Car with id {car_id} has been deleted'})
        except Car.DoesNotExist:
            return JsonResponse({'error': f'Car with id {car_id} does not exist'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CustomersView(View):
    def get(self, request):
        customers = Customer.objects.all()
        data = {'customers': list(customers.values())}
        return JsonResponse(data)

    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        customer = Customer(name=name, email=email, phone=phone)
        customer.save()
        data = {'message': f'Added customer with id {customer.id}'}
        return JsonResponse(data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CustomerInfoView(View):
    def get(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            data = {
                'id': customer.id,
                'name': customer.name,
                'email': customer.email,
                'phone': customer.phone
            }
            return JsonResponse(data)
        except Customer.DoesNotExist:
            return JsonResponse({'error': f'Customer with id {customer_id} does not exist'}, status=404)

    def put(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return JsonResponse({'error': f'Customer with id {customer_id} does not exist'}, status=404)

        data = json.loads(request.body)
        customer.name = data.get('name')
        customer.email = data.get('email')
        customer.phone_number = data.get('phone_number')
        customer.save()

        data = {'message': f'Updated customer with id {customer.id}'}
        return JsonResponse(data)

    def delete(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return JsonResponse({'error': f'Customer with id {customer_id} does not exist'}, status=404)

        customer.delete()
        data = {'message': f'Deleted customer with id {customer_id}'}
        return JsonResponse(data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class SalesView(View):
    def get(self, request):
        sales = Sale.objects.all()
        data = [
            {
                'id': sale.id,
                'car': sale.car_id,
                'customer': sale.customer_id,
                'date': sale.date,
                'price': sale.price
            } for sale in sales]
        return JsonResponse(data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        car_id = data.get('car_id')
        customer_id = data.get('customer_id')
        date = data.get('date')
        price = data.get('price')

        sale = Sale.objects.create(
            car_id=car_id,
            customer_id=customer_id,
            date=date,
            price=price
        )

        data = {
            'id': sale.id,
            'car_id': sale.car_id,
            'customer_id': sale.customer_id,
            'date': sale.date,
            'price': sale.price
        }
        return JsonResponse(data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class SaleInfoView(View):
    def get(self, request, sale_id):
        sale = Sale.objects.filter(id=sale_id).values('id', 'car', 'customer', 'date', 'price').first()
        if sale:
            return JsonResponse(sale)
        else:
            return JsonResponse({'error': f'Sale with id {sale_id} does not exist'}, status=404)

    def put(self, request, sale_id):
        data = json.loads(request.body)
        car_id = data.get('car_id')
        customer_id = data.get('customer_id')
        date = data.get('date')
        price = data.get('price')
        sale = Sale.objects.filter(id=sale_id).first()
        if sale:
            sale.car_id = car_id
            sale.customer_id = customer_id
            sale.date = date
            sale.price = price
            sale.save()
            data = {
                'id': sale.id,
                'car_id': sale.car_id,
                'customer_id': sale.customer_id,
                'date': sale.date,
                'price': sale.price
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': f'Sale with id {sale_id} does not exist'}, status=404)

    def delete(self, request, sale_id):
        sale = Sale.objects.filter(id=sale_id).first()
        if sale:
            sale.delete()
            return JsonResponse({'message': f'Sale with id {sale_id} has been deleted'})
        else:
            return JsonResponse({'error': f'Sale with id {sale_id} does not exist'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)
