# coding: utf8

from django.shortcuts import render
# from django.template import Context, loader

from .models import Product


def index(request):
    return render(request, 'pina/index.html')


def product_list(request):
    filter1 = Product.objects.filter(price__gte=3000)
    filter2 = Product.objects.filter(price__lt=3000)
    return render(
        request, 'pina/product_list.html',
        {'filter1': filter1, 'filter2': filter2})


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
