# coding: utf8

from django.shortcuts import render, redirect
from django.http import Http404
from django.forms import ModelForm

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


def product_delete_check(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404
    return render(
        request, 'pina/product_delete_check.html',
        {'product': product})


def product_delete(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.delete()
    except Product.DoesNotExist:
        raise Http404
    return render(
        request, 'pina/product_delete.html')


def product_entry(request):
    if request.method == 'POST':
        # POST データの束縛フォームの生成
        form = ProductForm(request.POST)
        # バリデーション（入力検証）通過
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            price = form.cleaned_data['price']

            product = Product(
                title=title, content=content, price=price,
                created_at="", updated_at="")
            product.save()
            # POST 後のリダイレクト
            return redirect('pina-product-entry-completion')
    else:
        # 非束縛フォーム生成（データが結びついてないフォーム)
        form = ProductForm()
    return render(request, 'pina/product_entry.html', {'form': form})


def product_entry_completion(request):
    return render(request, 'pina/product_entry_completion.html')
