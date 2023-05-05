from rest_framework import serializers
from cardealer.models import Car, Make, Customer, Sale


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['id', 'name', 'country']


class CarSerializer(serializers.ModelSerializer):
    make = MakeSerializer()

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'price')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone']


class SaleSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Sale
        fields = ['id', 'car', 'customer', 'date', 'price']

    def create(self, validated_data):
        car_data = validated_data.pop('car')
        customer_data = validated_data.pop('customer')
        car_serializer = CarSerializer(data=car_data)
        customer_serializer = CustomerSerializer(data=customer_data)

        if car_serializer.is_valid() and customer_serializer.is_valid():
            car = car_serializer.save()
            customer = customer_serializer.save()
            sale = Sale.objects.create(car=car, customer=customer, **validated_data)
            return sale
        else:
            raise serializers.ValidationError("Error creating sale")
