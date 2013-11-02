# coding: utf8

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    pdated_at = models.DateTimeField(auto_now=True)
