# coding: utf8

from django.shortcuts import render
from pina.forms import ProductForm
# from django.template import Context, loader
from django.http import Http404
from django.http import HttpResponseRedirect

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
    form = ProductForm()
    return render(request, 'pina/product_entry.html',
    {'form': form})

def product_entry_confirm(request):
    if request.method == 'POST': # フォームが提出された
        form = ProductForm(request.POST) # POST データの束縛フォームの生成
        if form.is_valid(): # バリデーション（入力検証）を通った
            t = form.cleaned_data['title']
            c = form.cleaned_data['content']
            p = form.cleaned_data['price']

            from datetime import datetime
            from .models import Product
            # created_at = models.DateTimeField(auto_now_add=True)
            # updated_at = models.DateTimeField(auto_now=True)
            p = Product(title=t, content=c, price=p, created_at="", updated_at="")
            p.save()
            return HttpResponseRedirect('completion') # POST 後のリダイレクト
    else:
        form = ProductForm() # 非束縛フォーム
    
    return render(request, 'pina/product_entry.html', {'form': form})

def product_entry_completion(request):
    return render(request, 'pina/product_entry_completion.html')
    
  
