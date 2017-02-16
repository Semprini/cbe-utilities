from django.db import models

from cbe.customer.models import Customer
from cbe.supplier_partner.models import Supplier, Buyer


class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory', null=True,blank=True)

    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)

    level = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductOffering(models.Model):
    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    sku = models.TextField()
    supplier_code = models.TextField(null=True, blank=True)

    categories = models.ManyToManyField('ProductCategory', blank=True)

    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, null=True, blank=True)
    buyer = models.ForeignKey(Buyer, null=True, blank=True)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    categories = models.ManyToManyField('ProductCategory', blank=True)
    products = models.ManyToManyField('ProductOffering', blank=True)
    customers = models.ManyToManyField(Customer, blank=True)

    def __str__(self):
        return self.name
