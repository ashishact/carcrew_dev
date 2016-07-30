from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = (
            'Product_Name',
            'Created',
            'Last_updated',
            'Product_Id',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = (
            'Category_Name',
            'Created',
            'Last_updated',
            'Category_Id',
            'Parent_Id',
        )


class CategoryDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CategoryDescription
        fields = (
            'Created',
            'Last_updated',
            'Category_Image_URL',
            'Category_Description',
        )


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Car
        fields = (
            'Car_Name',
            'Created',
            'Last_updated',
            'Car_Id',
            'Manufacturer_Name',
            'Model_Name',
            'Version',
            'Fuel_Type',
            'Transmission',
            'Year',
        )


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Manufacturer
        fields = (
            'Manufacturer_Name',
            'Created',
            'Last_updated',
            'Manufacturer_Id',
            'Manufacturer_Location',
        )


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = (
            'Name',
            'created',
            'last_updated',
            'Address_Street_Name',
            'Landmark',
            'Pin_Code',
            'City',
            'State',
            'Location',
        )


class GarageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Garage
        fields = (
            'Name',
            'Created',
            'Last_updated',
            'Garage_Name',
            'Garage_Id',
            'Year_of_Establishment',
            'Email_Id',
            'Opening_Time',
            'Closing_Time',
            'Days_of_Operation',
        )


