"""retail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from drf_nest.routers import AppRouter
from . import views

from cbe.party.urls import urlpatterns as PartyUrls
from cbe.location.urls import urlpatterns as LocationUrls
from utilities.product.urls import urlpatterns as ProductUrls

admin.site.site_title = 'CBE Utilities'
admin.site.site_header = 'Utilities Business Entities'

apps={  'party':'app-party',
        'location':'app-location',
        'product':'app-product',
}
router = AppRouter( apps=apps )

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + ProductUrls + PartyUrls + LocationUrls
