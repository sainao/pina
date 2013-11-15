# coding: utf8

from django.conf.urls import patterns, url
from pina.forms import ProductForm

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'pina.views.index', name='pina-index'),

    url(r'^products$', 'pina.views.product_list',
        name='pina-product-list'),

    url(r'^products/(?P<product_id>\d+)/$', 'pina.views.product_detail',
        name='pina-product-detail'),

    url(r'^products/(?P<product_id>\d+)/check$',
        'pina.views.product_delete_check',
        name='pina-product-delete-check'),

    url(r'^products/(?P<product_id>\d+)/delete$',
        'pina.views.product_delete',
        name='pina-product-delete'),

    url(r'^products/entry$', 'pina.views.product_entry',
        name='pina-product-entry'),


)
