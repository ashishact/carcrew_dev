from . import models, serializers
from rest_framework import generics, permissions


# Product
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarList(generics.ListCreateAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDescriptionList(generics.ListCreateAPIView):
    queryset = models.CategoryDescription.objects.all()
    serializer_class = serializers.CategoryDescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryDescription.objects.all()
    serializer_class = serializers.CategoryDescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ManufacturerList(generics.ListCreateAPIView):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressList(generics.ListCreateAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class GarageList(generics.ListCreateAPIView):
    queryset = models.Garage.objects.all()
    serializer_class = serializers.GarageSerializer
    permission_classes = [permissions.IsAuthenticated]


class GarageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Garage.objects.all()
    serializer_class = serializers.GarageSerializer
    permission_classes = [permissions.IsAuthenticated]
