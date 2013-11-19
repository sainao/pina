# coding: utf8
from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(max_length=300, label=u'商品名')
    content = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
