from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator #feild included for phone number


class CommaSepField(models.Field):
    "Implements comma-separated storage of lists"

    def __init__(self, separator=",", *args, **kwargs):
        self.separator = separator
        super(CommaSepField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CommaSepField, self).deconstruct()
        # Only include kwarg if it's not the default
        if self.separator != ",":
            kwargs['separator'] = self.separator
        return name, path, args, kwargs


# Create your models here.


class Car(models.Model):

    MANUFACTURER_LIST = (
        (1, 'Maruti'),
        (2, 'Hyundai'),
        (3, 'Tata Motors'),
        (4, 'Mahindra and Mahindra'),
        (5, 'Toyota'),
        (6, 'Honda'),
        (7, 'Chevrolet'),
        (8, 'Volkswagen'),
        (9, 'Skoda'),
        (10, 'Fiat'),
        (11, 'Renault'),
    )

    TYPE_CHOICES = (
        (1, 'Petrol'),
        (2, 'Diesel'),
        (3, 'CNG/LPG Company Fitted'),
        (4, 'CNG/LPG Externally Fitted'),
        (5, 'Electric'),
    )

    # car_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="chasis number must be entered in the format: 'MALA351ALDM165832B'. Up to 19 digits allowed.")
    car_regex = RegexValidator(regex=r'^MA[A-HJ-NPR-Z0-9]{15}$', message="chasis number must be entered in the format: 'MALA351ALDM165832B'. Up to 19 digits allowed.")

    Car_Chasis_Number = models.CharField(max_length=19, validators=[car_regex], blank=True, )  # validators should be a list
    Car_Manufacture = models.IntegerField(
        choices=MANUFACTURER_LIST,
        default=None,
    )

    Model = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    Transmission = models.IntegerField(
        choices=TYPE_CHOICES,
        default=None,
    )
    Year_of_Manufacture = models.IntegerField(choices=[(i, i) for i in range(1950, 2017)], blank=True)
    Number_of_Service = models.PositiveIntegerField(default=0)
    Number_of_KMs = models.PositiveIntegerField(default=0)
    Registration_Number = models.CharField(max_length=255)
    Engine_Number = models.CharField(max_length=255)

    def __str__(self):
        return self.Car_Chasis_Number


class Product(models.Model):
    CATEGORY_CHOICES = (
        (1, 'Engine'),
        (2, 'Electrical'),
        (3, 'Brakes'),
        (4, 'Suspension'),
        (5, 'Transmission'),
        (6, 'Body'),
        (7, 'Heating_Ventilation_Ac'),
    )
    STATUS_CHOICES = (
        (1, 'available'),
        (2, 'Out of stock'),
    )

    Product_ID = models.IntegerField(auto_created=True, primary_key=True)
    Product_Name = models.CharField(max_length=500)
    Manufacture_Name = models.CharField(max_length=500, blank=True)
    Supplier_Name = models.CharField(max_length=500, blank=False)
    Date_of_purchase = models.DateField(blank=True)
    Status=models.IntegerField(
        choices=STATUS_CHOICES,
        default=None,
    )
    Price = models.FloatField()
    Discount = models.FloatField()
    Final_Price = models.FloatField()
    SKU_Number = models.CharField(max_length=255)
    Meta_Description = models.TextField(max_length=10000)
    Meta_Keyword = models.CharField(max_length=255)

    Category = models.IntegerField(
        choices=CATEGORY_CHOICES,
        default=None,
    )
    Sub_Category = models.IntegerField(
        choices=CATEGORY_CHOICES,
        default=None,
    )
    Image = models.URLField()
    # Tags = CommaSepField(default='Ashish')
    Compatible_Car = models.ForeignKey(Car, related_name='compatible_car')
    Original_Car = models.ForeignKey(Car, related_name='original_car')

    def __str__(self):
        return self.Product_Name


class Garage(models.Model):

    SERVICES = (

        (1, 'Washing'),
        (2, 'Hard_wash'),
        (3, 'Cold_wash'),

    )

    Garage_Name = models.CharField(max_length=500)
    Garage_ID = models.IntegerField(primary_key=True)
    Garage_Location = models.CharField(max_length=255, blank=True)
    Number_Post_Lift = models.IntegerField(blank=True)
    Garage_Area = models.IntegerField(blank=True)
    Number_Mechanic = models.IntegerField(blank=True)
    Field_of_Expertise = models.IntegerField(
        choices=SERVICES,
        default=None,

    )
    Number_of_Advisor = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list

    def __str__(self):
        return self.Garage_Name