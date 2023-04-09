from django.http import JsonResponse
from django.views import View


class CarsView(View):
    def get(self, request):
        data = {'message': 'This is a get_cars method.'}
        return JsonResponse(data)

    def post(self, request):
        data = {'message': 'This is an add_car method.'}
        return JsonResponse(data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CarInfoView(View):
    def get(self, request, car_id):
        data = {'message': f'This is a get_car method with id {car_id}.'}
        return JsonResponse(data)

    def put(self, request, car_id):
        data = {'message': f'This is an update_car method with id {car_id}.'}
        return JsonResponse(data)

    def delete(self, request, car_id):
        data = {'message': f'This is a delete_car method with id {car_id}.'}
        return JsonResponse(data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CustomersView(View):
    def get(self, request):
        data = {'message': 'This is a get_customers method.'}
        return JsonResponse(data)

    def post(self, request):
        data = {'message': 'This is an add_customer method.'}
        return JsonResponse(data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CustomerInfoView(View):
    def get(self, request, customer_id):
        data = {'message': f'This is a get_customer method with id {customer_id}.'}
        return JsonResponse(data)

    def put(self, request, customer_id):
        data = {'message': f'This is an update_customer method with id {customer_id}.'}
        return JsonResponse(data)

    def delete(self, request, customer_id):
        data = {'message': f'This is a delete_customer method with id {customer_id}.'}
        return JsonResponse(data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class SalesView(View):
    def get(self, request):
        data = {'message': 'This is a get_sales method.'}
        return JsonResponse(data)

    def post(self, request):
        data = {'message': 'This is an add_sale method.'}
        return JsonResponse(data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class SaleInfoView(View):
    def get(self, request, sale_id):
        data = {'message': f'This is a get_sale method with id {sale_id}.'}
        return JsonResponse(data)

    def put(self, request, sale_id):
        data = {'message': f'This is an update_sale method with id {sale_id}.'}
        return JsonResponse(data)

    def delete(self, request, sale_id):
        data = {'message': f'This is a delete_sale method with id {sale_id}.'}
        return JsonResponse(data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)