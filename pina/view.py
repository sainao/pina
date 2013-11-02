# coding: utf8

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

from pina.models import Product

def index(request):
    return render(request, 'pina/index.html')
