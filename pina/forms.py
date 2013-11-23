# coding: utf8

from django import forms
from django.forms import ModelForm

from .models import Product


class ProductForm(ModelForm):
    title = forms.CharField(label=u'商品名', max_length=10)
    content = forms.CharField(label=u'説明', widget=forms.Textarea)
    price = forms.IntegerField(label=u'価格')

    class Meta:
        model = Product
        fields = ('title', 'content', 'price')

