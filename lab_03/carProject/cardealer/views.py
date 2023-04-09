# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def cars(request):
    if request.method == 'GET':
        data = {'message': 'This is a get_cars method.'}
        return JsonResponse(data)
    elif request.method == 'POST':
        data = {'message': 'This is a add_car method.'}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def car_info(request, car_id):
    if request.method == 'GET':
        data = {'message': f'This is a get_car method with id {car_id}.'}
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = {'message': f'This is a update_car method with id {car_id}.'}
        return JsonResponse(data)
    if request.method == 'DELETE':
        data = {'message': f'This is a delete_car method with id {car_id}.'}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def customers(request):
    if request.method == 'GET':
        data = {'message': 'This is a get_customers method.'}
        return JsonResponse(data)
    elif request.method == 'POST':
        data = {'message': 'This is a add_customer method.'}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def customer_info(request, customer_id):
    if request.method == 'GET':
        data = {'message': f'This is a get_customer method with id {customer_id}.'}
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = {'message': f'This is a update_customer method with id {customer_id}.'}
        return JsonResponse(data)
    elif request.method == 'DELETE':
        data = {'message': f'This is a delete_customer method with id {customer_id}.'}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def sales(request):
    if request.method == 'GET':
        data = {'message': 'This is a get_sales method.'}
        return JsonResponse(data)
    elif request.method == 'POST':
        data = {'message': 'This is a add_sale method.'}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def sale_info(request, sale_id):
    if request.method == 'GET':
        data = {'message': f'This is a get_sales method with id {sale_id}.'}
        return JsonResponse(data)
    if request.method == 'PUT':
        data = {'message': f'This is a update_sale method with id {sale_id}.'}
        return JsonResponse(data)
    if request.method == 'DELETE':
        data = {'message': f'This is a delete_sale method with id {sale_id}.'}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
