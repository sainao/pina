# coding: utf8

from django.db import models


class Product(models.Model):
    title = models.CharField(u'商品名', max_length=100)
    content = models.TextField(u'説明')
    price = models.IntegerField(u'価格')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
