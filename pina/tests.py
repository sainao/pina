# coding=utf8

from django.test import TestCase, Client
from django.db import models

from .models import Product


class Product(models.Model):
    title = models.CharField(u'商品名', max_length=100)
    content = models.TextField(u'説明')
    price = models.IntegerField(u'価格')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class PinaTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_list(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        product = Product(title='ナオコ', content=u'サイトー', price=5000)
        product.save()

        response = self.client.get('/products/{0}/'.format(product.id))
        self.assertEqual(response.status_code, 200)

        product.delete()

        response = self.client.get('/products/{0}/'.format(product.id))
        self.assertEqual(response.status_code, 404)

        response = self.client.post('/products/{0}/'.format(product.id))
        self.assertEqual(response.status_code, 404)
