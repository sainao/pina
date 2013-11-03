# coding: utf8

from django.shortcuts import render
# from django.template import Context, loader

from .models import Product


def index(request):
    return render(request, 'pina/index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'pina/product_list.html', {'products': products})
