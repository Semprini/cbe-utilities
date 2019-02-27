"""product URL Configuration

"""
from django.conf.urls import include, url

from drf_nest.routers import AppRouter
from . import views

import utilities.product.views as ProductViews

router = AppRouter(root_view_name='app-product')
router.register(r'product/product_offering', ProductViews.ProductOfferingViewSet)
router.register(r'product/product_category', ProductViews.ProductCategoryViewSet)
router.register(r'product/promotion', ProductViews.PromotionViewSet)

urlpatterns = [
    url(r'^api/product/', include(router.urls)),
]

