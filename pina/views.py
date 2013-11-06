# coding: utf8

from django.shortcuts import render
# from django.template import Context, loader

from .models import Product


def index(request):
    return render(request, 'pina/index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'pina/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'pina/product_detail.html', {'product': product})


def product_delete_check(request, product_id):
    check_product = Product.objects.get(pk=product_id)
    return render(
        request, 'pina/product_delete_check.html',
        {'check_product': check_product})


def product_delete(request, product_id):
    product = Product.objects.get(pk=product_id)
    delete_product = product.delete()
    return render(
        request, 'pina/product_delete.html',
        {'delete_product': delete_product})


def product_register(request):
    return render(request, 'pina/product_register.html')


def product_register_check(request):
    product = Product.objects.get(pk=product.id)
    create_product = product.create()
    
    return render(request, 'pina/product_register_check.html')
