from django.db import models

# Create your models here.

# Products

# consult http://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/
#         https://docs.djangoproject.com/en/1.9/ref/models/fields/#choices
CATEGORY_CHOICES = (
    (1, 'ENGINE'),
    (2, 'BRAKES'),
    (3, 'TRANSMISSION'),
    (4, 'SUSPENSION'),
    (5, 'BODY'),
    (6, 'ELECTRICAL'),
    (7, 'HEATING VENTILATION & A'),
)

SUBCATEGORY_CHOICES = (
    (1, 'FILTERS'),
)


class Product(models.Model):
    Id = models.IntegerField(unique=True, null=False, primary_key=True, editable=False)
    name = models.CharField(max_length=200)

    manufacturerName = models.CharField(max_length=200)
    # manufacturerLocation = models.PointField(help_text='Represented as (longitude, latitude)')
    manufacturerLat = models.DecimalField(max_digits=10, decimal_places=6)
    manufacturerLon = models.DecimalField(max_digits=10, decimal_places=6)

    supplierName = models.CharField(max_length=200)
    dateOfPurchase = models.DateTimeField(auto_now_add=True)
    availability = models.BooleanField(default=False)
    price = models.FloatField()
    discount = models.FloatField()
    skuNo = models.IntegerField()
    metaDescription = models.TextField()
    # metaKeywords = models.

    category = models.IntegerField(choices=CATEGORY_CHOICES)
    subcategory = models.IntegerField(choices=SUBCATEGORY_CHOICES)
    imageUrl = models.URLField(default='default.jpg')

    class Meta:
        ordering = ('name',)
