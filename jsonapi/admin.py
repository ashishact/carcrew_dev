from django.contrib import admin

# Register your models here.

from .models import Car, Product, Garage

admin.site.register(Car)
admin.site.register(Product)
admin.site.register(Garage)
