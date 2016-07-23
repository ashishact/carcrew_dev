from rest_framework import serializers
from .models import Product, CATEGORY_CHOICES, SUBCATEGORY_CHOICES


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'Id',
            'name',
            'manufacturerName',
            'manufacturerLat',
            'manufacturerLon',
            'supplierName',
            'dateOfPurchase',
            'availability',
            'price',
            'discount',
            'skuNo',
            'metaDescription',
            'category',
            'subcategory',
            'imageUrl'
        )
