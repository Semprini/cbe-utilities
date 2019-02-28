from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'utilities.product'

    def ready(self):
        import drf_nest.signals
        from utilities.product.models import ProductOffering
        from utilities.product.serializers import ProductOfferingSerializer

        exchange_prefix = settings.MQ_FRAMEWORK['EXCHANGE_PREFIX'] + self.name
        exchange_header_list = ('status',)
        
        post_save.connect(  drf_nest.signals.notify_extra_args(   serializer=ProductOfferingSerializer, 
                                                                exchange_prefix=exchange_prefix + ".ProductOffering", 
                                                                exchange_header_list=exchange_header_list)(drf_nest.signals.notify_save_instance), 
                            sender=ProductOffering, weak=False)

