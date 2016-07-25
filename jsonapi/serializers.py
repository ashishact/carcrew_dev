from rest_framework import serializers
from .models import Car, Product, Garage


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'Car_Chasis_Number',
            # 'Car_Manufacturer',
            'Model',
            'Fuel_Type',
            'Transmission',
            'Year_of_Manufacture',
            'Number_of_Service',
            'Number_of_KMs_Travelled',
            'Registration_Number',
            'Engine_Number',
        )


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'Product_ID',
            'Product_Name',
            'Manufacture_Name',
            'Supplier_Name',
            'Date_of_purchase',
            'Status',
            'Price',
            'Discount',
            'Final_Price',
            'SKU_Number',
            'Meta_Description',
            'Meta_Keyword',
            'Category',
            'Sub_Category',
            'Image',
            'Compatible_Car',
            'Original_Car',
        )


class GarageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = (
            'Garage_Name',
            'Garage_ID',
            'Garage_Location',
            'Number_of_Two_Post_Lift',
            'Garage_Area',
            'Number_of_Mechanic',
            'Field_of_Expertise',
            'Number_of_Advisor',
            'Phone_Number_Primary',
            'Phone_Number_Secondary',
        )