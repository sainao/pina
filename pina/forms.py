# coding: utf8

from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(label=u'商品名', max_length=300)
    content = forms.CharField(label=u'説明', widget=forms.Textarea)
    price = forms.IntegerField(label=u'価格')
