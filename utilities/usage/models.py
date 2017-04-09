from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from gm2m import GM2MField

from utilities.product.models import ProductPrice

class Usage(models.Model):
    usage_date = models.DateTimeField()
    usage_status = models.CharField(max_length=100)
    party_roles = GM2MField(related_name="usage_party_roles")
    usage_specification = GM2MField(related_name="usage_usage_specification")
    product_prices = models.ManyToManyField(ProductPrice, blank=True)
    #TODO: place
    
    class Meta:
        abstract = True


class UsageSpecification(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    lifecycle_status = models.CharField(max_length=200, blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class UsageSpecCharacteristic(models.Model):
    usage_specification_content_type = models.ForeignKey(
        ContentType, related_name="%(app_label)s_%(class)s_ownership")
    usage_specification_object_id = models.PositiveIntegerField()    
    usage_specification = GenericForeignKey('usage_specification_content_type', 'usage_specification_object_id')

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)

    # Shortcut usage spec characteristic value
    value_type = models.CharField(max_length=200, blank=True, null=True)
    unit_of_measure = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    value_from = models.CharField(max_length=200, blank=True, null=True)
    value_to = models.CharField(max_length=200, blank=True, null=True)
    range_interval = models.CharField(max_length=200, blank=True, null=True)
    default = models.NullBooleanField(blank=True, null=True)


class VoiceCallUsage(Usage):
    originationAddress = models.CharField(max_length=100)
    destinationAddress = models.CharField(max_length=100)

    call_duration = models.DurationField()
    call_type = models.CharField(max_length=100)

    
class UsageCharacteristicValue(models.Model):
    value = models.CharField(max_length=200, blank=True, null=True)
    value_from = models.CharField(max_length=200, blank=True, null=True)
    value_to = models.CharField(max_length=200, blank=True, null=True)

    usage_content_type = models.ForeignKey(
        ContentType, related_name="%(app_label)s_%(class)s_ownership")
    usage_object_id = models.PositiveIntegerField()    
    usage = GenericForeignKey('usage_content_type', 'usage_object_id')

    usage_spec_characteristic = models.ForeignKey(UsageSpecCharacteristic)