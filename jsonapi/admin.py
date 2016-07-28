from django.contrib import admin

from .models import Car, Product, Brand, Garage, Manufacturer, Address, Category, CategoryDescription
from .utilmodels import LatLon
# Register your models here.
admin.site.register(Car)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Garage)
admin.site.register(Manufacturer)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(CategoryDescription)

# Utis
admin.site.register(LatLon)

