# coding: utf8

from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'pina.views.index', name='pina-index'),
    url(r'^products$', 'pina.views.product_list', name='pina-product-list'),
    url(r'^products/(?P<product_id>\d+)/$', 'pina.views.product_detail',
        name='pina-product-detail'),
    #url(r'^products/register$', 'pina.views.product_register',
    #    name='pina-product-register'),
)
