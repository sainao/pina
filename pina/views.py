# coding: utf8

from django.shortcuts import render, redirect
from django.http import Http404

from .forms import ProductForm
from .models import Product


def index(request):
    return render(request, 'pina/index.html')


def product_list(request):
    price_lt_3000 = Product.objects.filter(price__lt=3000)
    price_gte_3000 = Product.objects.filter(price__gte=3000)
    return render(
        request, 'pina/product_list.html',
        {'price_lt_3000': price_lt_3000,
            'price_gte_3000': price_gte_3000})


def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'pina/product_detail.html', {'product': product})


def product_edit(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product = form.save()
                return redirect('pina-product-detail', product.id)
        else:
            form = ProductForm(instance=product)
    except Product.DoesNotExist:
        raise Http404
    return render(
        request, 'pina/product_edit.html',
        {'form': form, 'product': product})


def product_delete_check(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        if request.method == 'POST':
            product.delete()
            return redirect('pina-product-delete')
    except Product.DoesNotExist:
        raise Http404
    return render(
        request, 'pina/product_delete_check.html', {'product': product})


def product_delete(request):
    return render(request, 'pina/product_delete.html')


def product_entry(request):
    if request.method == 'POST':
        # POST データの束縛フォームの生成
        form = ProductForm(request.POST)
        # バリデーション（入力検証）通過
        if form.is_valid():
            form.save()
            return redirect('pina-product-list')
    else:
        # データが結びついてないフォーム
        form = ProductForm()
    return render(request, 'pina/product_entry.html', {'form': form})
