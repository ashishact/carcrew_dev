# from django.shortcuts import render
from django.http import HttpResponse, Http404


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from jsonapi.models import Car, Product,  Garage
from jsonapi.serializers import CarSerializers, ProductSerializers, GarageSerializers

# Create your views here.


def index(request):
    return HttpResponse("<h1>THIS IS JSON API</h1>")

# Shortcuts #######################################
# from django.shortcuts import render_to_response
#
#
# def index(request):
#     return render_to_response('public/index.html')
###################################################


# Cars ######################################################
class CarList(APIView):
    """
    List all cars, or create a new car.
    """

    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializers(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetail(APIView):
    """
    send details of a car
    """
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializers(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializers(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Product ######################################################
class ProductList(APIView):
    """
    List all cars, or create a new car.
    """

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    send details of a car
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Garage ######################################################
class GarageList(APIView):
    """
    List all cars, or create a new car.
    """

    def get(self, request, format=None):
        garages = Garage.objects.all()
        serializer = GarageSerializers(garages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GarageDetail(APIView):
    """
    send details of a car
    """
    def get_object(self, pk):
        try:
            return Garage.objects.get(pk=pk)
        except Garage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializers(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializers(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        garage = self.get_object(pk)
        garage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)