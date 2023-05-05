from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from cardealer.models import Car, Customer, Make, Sale
from cardealer.serializers import CarSerializer, CustomerSerializer, SaleSerializer, MakeSerializer


class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'ok'}, status=200)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CarSearchView(APIView):
    def get(self, request):
        make = request.GET.get('make')
        model = request.GET.get('model')
        if make and model:
            cars = Car.objects.filter(make__name__icontains=make, model__icontains=model)
        elif make:
            cars = Car.objects.filter(make__name__icontains=make)
        elif model:
            cars = Car.objects.filter(model__icontains=model)
        else:
            cars = Car.objects.none()

        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CarsView(APIView):
    queryset = Car.objects.all()

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            make_data = serializer.validated_data.pop('make')
            make, _ = Make.objects.get_or_create(**make_data)
            car = Car.objects.create(make=make, **serializer.validated_data)
            serializer = CarSerializer(car)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CarInfoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except Car.DoesNotExist:
            return Response({'error': f'Sale with id {kwargs["id"]} does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except Car.DoesNotExist:
            return Response({'error': f'Sale with id {kwargs["id"]} does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except Car.DoesNotExist:
            return Response({'error': f'Sale with id {kwargs["id"]} does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CustomersView(APIView):
    queryset = Customer.objects.all()

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'message': f'Added customer with id {serializer.data["id"]}'}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CustomerInfoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except Customer.DoesNotExist:
            return Response({'error': f'Customer with id {kwargs["id"]} does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except Customer.DoesNotExist:
            return Response({'error': f'Customer with id {kwargs["id"]} does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except Customer.DoesNotExist:
            return Response({'error': f'Customer with id {kwargs["id"]} does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class SalesView(APIView):
    queryset = Sale.objects.all()

    def get(self, request):
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SaleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class SaleInfoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except Sale.DoesNotExist:
            return Response({'error': f'Sale with id {kwargs["id"]} does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except Sale.DoesNotExist:
            return Response({'error': f'Sale with id {kwargs["id"]} does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except Sale.DoesNotExist:
            return Response({'error': f'Sale with id {kwargs["id"]} does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
