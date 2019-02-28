from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'utilities.product'

    def ready(self):
        import drf_nest.signals
        from utilities.product.models import Product
        from utilities.product.serializers import ProductSerializer

        exchange_prefix = settings.MQ_FRAMEWORK['EXCHANGE_PREFIX'] + self.name
        exchange_header_list = ('status',)
        
        post_save.connect(  drf_nest.signals.notify_extra_args(   serializer=ProductSerializer, 
                                                                exchange_prefix=exchange_prefix + ".Product", 
                                                                exchange_header_list=exchange_header_list)(drf_nest.signals.notify_save_instance), 
                            sender=Product, weak=False)

