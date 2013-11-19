# coding: utf8
from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=300)
    price = forms.IntegerField()
