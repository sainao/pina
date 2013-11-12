# coding: utf8

from django.shortcuts import render
# from django.template import Context, loader

from .models import Product


def index(request):
    return render(request, 'pina/index.html')


def product_list(request):
    products_of_lower = Product.objects.filter(price__lt=3000)
    products_higher = Product.objects.filter(price__gte=3000)
    return render(
        request, 'pina/product_list.html',
        {'products_of_lower': products_of_lower, 'products_higher': products_higher})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'pina/product_detail.html', {'product': product})


def product_delete_check(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(
        request, 'pina/product_delete_check.html',
        {'product': product})


def product_delete(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return render(
        request, 'pina/product_delete.html')
