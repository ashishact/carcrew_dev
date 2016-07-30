from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db import fields as extension_fields

from .utilmodels import LatLon


class Brand(models.Model):
    # Fields
    Brand_Id = models.PositiveIntegerField(primary_key=True)
    Brand_Name = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.Brand_Name


class Car(models.Model):

    # Fields
    Car_Name = models.CharField(max_length=1000)
    # slug = extension_fields.AutoSlugField(populate_from='Car_Name', blank=True)
    Created = models.DateTimeField(auto_now_add=True, editable=False)
    Last_updated = models.DateTimeField(auto_now=True, editable=False)
    Car_Id = models.PositiveIntegerField(primary_key=True)
    Manufacturer_Name = models.IntegerField()  # Take data from manufacturer names
    Model_Name = models.IntegerField()  # Take data from list of Model Names
    Version = models.IntegerField()  # Take data from list of Version name
    Fuel_Type = models.IntegerField()
    Transmission = models.IntegerField()
    Year = models.DateField()

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return self.Car_Name

    # def get_absolute_url(self):
    #     return reverse('cars_detail', args=(self.slug,))
    #
    # def get_update_url(self):
    #     return reverse('cars_update', args=(self.slug,))


class Product(models.Model):

    # Fields
    Product_Name = models.CharField(max_length=255)
    # slug = extension_fields.AutoSlugField(populate_from='', blank=True)
    Created = models.DateTimeField(auto_now_add=True, editable=False)
    Last_updated = models.DateTimeField(auto_now=True, editable=False)
    Product_Id = models.PositiveIntegerField(primary_key=True)
    # Brand_Id = models.ForeignKey(Brand)
    Product_Unique_Name = models.CharField(max_length=1000)

    # Relationship Fields
    Brand_id = models.ForeignKey(Brand, )
    Compatible_Car = models.ForeignKey(Car, )

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return self.Product_Name

    # def get_absolute_url(self):
    #     return reverse('products_detail', args=(self.slug,))
    #
    # def get_update_url(self):
    #     return reverse('products_update', args=(self.slug,))


class Manufacturer(models.Model):

    # Fields
    Manufacturer_Name = models.CharField(max_length=1000)
    # slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    Created = models.DateTimeField(auto_now_add=True, editable=False)
    Last_updated = models.DateTimeField(auto_now=True, editable=False)
    Manufacturer_Id = models.PositiveIntegerField(primary_key=True)
    Manufacturer_Location = models.ForeignKey(LatLon, )

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return self.Manufacturer_Name
    #
    # def get_absolute_url(self):
    #     return reverse('manufacturer_detail', args=(self.slug,))
    #
    # def get_update_url(self):
    #     return reverse('manufacturer_update', args=(self.slug,))


class Category(models.Model):

    # Fields
    Category_Name = models.CharField(max_length=1000)
    # slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    Created = models.DateTimeField(auto_now_add=True, editable=False)
    Last_updated = models.DateTimeField(auto_now=True, editable=False)
    Category_Id = models.PositiveIntegerField(primary_key=True)
    Parent_Id = models.PositiveIntegerField(unique=True)

    # Relationship Fields
    Product_Id = models.ForeignKey(Product, )
    Manufacturer_Id = models.ForeignKey(Manufacturer, )

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return self.Category_Name

    # def get_absolute_url(self):
    #     return reverse('category_detail', args=(self.slug,))
    #
    # def get_update_url(self):
    #     return reverse('category_update', args=(self.slug,))


class CategoryDescription(models.Model):

    # Fields
    # slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    Created = models.DateTimeField(auto_now_add=True, editable=False)
    Last_updated = models.DateTimeField(auto_now=True, editable=False)
    Category_Image_URL = models.CharField(max_length=1000)
    Category_Description = models.TextField(max_length=1000)
    Category_Description_Id = models.PositiveIntegerField(primary_key=True, auto_created=True)

    # Relationship Fields
    Category_Id = models.ForeignKey(Category, )

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return self.Category_Description_Id

    # def get_absolute_url(self):
    #     return reverse('category_description_detail', args=(self.slug,))
    #
    # def get_update_url(self):
    #     return reverse('category_description_update', args=(self.slug,))


class Address(models.Model):

    # Fields
    Address_Id = models.PositiveIntegerField(primary_key=True, auto_created=True)
    Name = models.CharField(max_length=1000)
    # slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    Created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Address_Street_Name = models.CharField(max_length=1000)
    Landmark = models.CharField(max_length=1000)
    Pin_Code = models.IntegerField()
    City = models.IntegerField()
    State = models.IntegerField()
    Location = models.IntegerField()

    # Relationship Fields
    Manufacturer_Id = models.ForeignKey(Manufacturer, )

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return self.Name

    # def get_absolute_url(self):
    #     return reverse('address_detail', args=(self.slug,))
    #
    # def get_update_url(self):
    #     return reverse('address_update', args=(self.slug,))


class Garage(models.Model):

    # Fields
    Garage_Id = models.PositiveIntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    # slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    Created = models.DateTimeField(auto_now_add=True, editable=False)
    Last_updated = models.DateTimeField(auto_now=True, editable=False)
    Garage_Name = models.CharField(max_length=1000)
    Year_of_Establishment = models.DateField()
    Email_Id = models.CharField(max_length=1000)
    Opening_Time = models.TimeField()
    Closing_Time = models.TimeField()
    Days_of_Operation = models.PositiveIntegerField()
    Address = models.ForeignKey(Address, default=1)

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return self.Name

    # def get_absolute_url(self):
    #     return reverse('garage_detail', args=(self.slug,))
    #
    # def get_update_url(self):
    #     return reverse('garage_update', args=(self.slug,))


