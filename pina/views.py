# coding: utf8

from django.shortcuts import render
# from django.template import Context, loader

from .models import Product


def index(request):
    return render(request, 'pina/index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'pina/product_list.html', {'products': products})


def product_price_filter1(request):
    filter1 = Product.objects.filter(price__gte=3000)
    return render(
        request, 'pina/product_price_filter1.html',
        {'filter1': filter1})


def product_price_filter2(request):
    filter2 = Product.objects.filter(price__lt=3000)
    return render(
        request, 'pina/product_price_filter2.html',
        {'filter2': filter2})


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


# def product_entry(request):
#    product = Product.objects.get(pk=product_id)
#    return render(request, 'pina/product_entry.html', {'product': product})


# def product_entry_confirm(request, prduct_id):
#    new_product = Product.objects.get(pk=product_id)
#    new_product.save()
#    return render(request,
#        'pina/product_entry_confirm.html',
#        {'new_product': new_product})
