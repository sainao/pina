# coding: utf8

from django.shortcuts import render
from pina.forms import ProductForm
from django.http import Http404
from django.shortcuts import redirect

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
    return render(
        request, 'pina/product_entry.html',
        {'form': form})


def product_entry_confirm(request):
    if request.method == 'POST':  # フォームが提出された
        form = ProductForm(request.POST)  # POST データの束縛フォームの生成
        if form.is_valid():  # バリデーション（入力検証）を通った
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            price = form.cleaned_data['price']

            p = Product(
                title=title, content=content, price=price,
                created_at="", updated_at="")
            p.save()
            # 入力検証が済み、作成日時や更新日時を保存し、完了ページへ移動する
            # POST 後のリダイレクト
            return redirect('pina.views.product_entry_completion')
    else:
        form = ProductForm()  # 非束縛フォーム
    # 未記入がある際に入力された中途半端なデータを~confirm.htmlへ渡す
    return render(request, 'pina/product_entry_confirm.html', {'form': form})


def product_entry_completion(request):
    return render(request, 'pina/product_entry_completion.html')
