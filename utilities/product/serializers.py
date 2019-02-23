from urllib.parse import urlparse

from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers

from drf_nest.serializer_fields import TypeField
from utilities.product.models import ProductOffering, ProductCategory, Promotion


class ProductOfferingSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

    class Meta:
        model = ProductOffering
        fields = ('type', 'url', 'valid_from', 'valid_to', 'name',
                  'description', 'sku', 'categories', 'retail_price','supplier','buyer')


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

    class Meta:
        model = ProductCategory
        fields = ('type', 'url', 'valid_from', 'valid_to', 'parent', 'level', 'name',
                  'description', )


class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

    class Meta:
        model = Promotion
        fields = ('type', 'url', 'valid_from', 'valid_to', 'name',
                  'description', 'categories', 'products','customers')
