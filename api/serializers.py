from rest_framework import serializers
from .models import Product, CATEGORY_CHOICES, SUBCATEGORY_CHOICES


# class ProductSerializers(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     Id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200)
#     manufacturerName = serializers.CharField(max_length=200)
#     manufacturerLat = serializers.DecimalField(max_digits=10, decimal_places=6)
#     manufacturerLon = serializers.DecimalField(max_digits=10, decimal_places=6)
#
#     supplierName = serializers.CharField(max_length=2000)
#     dateOfPurchase = serializers.DateTimeField(auto_now_add=True)
#     availability = serializers.BooleanField(default=False)
#     price = serializers.FloatField()
#     discount = serializers.FloatField()
#     skuNo = serializers.IntegerField()
#     metaDescription = serializers.CharField(style={'base_template': 'textarea.html'})
#
#     category = serializers.ChoiceField(choices=CATEGORY_CHOICES)
#     subcategory = serializers.ChoiceField(choices=SUBCATEGORY_CHOICES)
#
#     imageUrl = serializers.URLField(default='default.jpg')
#
#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.manufacturerName = validated_data.get('manufacturerName', instance.manufacturerName)
#         instance.manufacturerLat = validated_data.get('manufacturerLat', instance.manufacturerLat)
#         instance.manufacturerLon = validated_data.get('manufacturerLon', instance.manufacturerLon)
#         instance.supplierName = validated_data.get('supplierName', instance.supplierName)
#         instance.dateOfPurchase = validated_data.get('dateOfPurchase', instance.dateOfPurchase)
#         instance.availability = validated_data.get('availability', instance.availability)
#         instance.price = validated_data.get('price', instance.price)
#         instance.discount = validated_data.get('discount', instance.discount)
#         instance.skuNo = validated_data.get('skuNo', instance.skuNo)
#         instance.metaDescription = validated_data.get('metaDescription', instance.metaDescription)
#         instance.category = validated_data.get('category', instance.category)
#         instance.subcategory = validated_data.get('subcategory', instance.subcategory)
#         instance.imageUrl = validated_data.get('imageUrl', instance.imageUrl)
#         instance.save()
#         return instance


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
