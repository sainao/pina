# coding=utf8

from django.test import TestCase, Client

from .models import Product


from django.db import models


class Product(models.Model):
    title = models.CharField(u'商品名', max_length=100)
    content = models.TextField(u'説明')
    price = models.IntegerField(u'価格')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class PinaTest(TestCase):

    # setUp は各テストメソッドの実行前に必ず実行されるメソッド
    def setUp(self):
        self.client = Client()

    # テストメソッド名は必ず test で始める
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


    def test_product_edit(self):
        product = Product(title='ナオコ', content=u'サイトー', price=5000)
        product.save()

        response = self.client.get('/products/{0}/edit'.format(product.id))
        self.assertEqual(response.status_code, 200)

        product.delete()

        response = self.client.get('/products/{0}/edit'.format(product.id))
        self.assertEqual(response.status_code, 404)

        response = self.client.post('/products/{0}/edit'.format(product.id))
        self.assertEqual(response.status_code, 404)


    def test_product_delete_check(self):
        product = Product(title='ナオコ', content=u'サイトー', price=5000)
        product.save()

        response = self.client.get('/products/{0}/check'.format(product.id))
        self.assertEqual(response.status_code, 200)

        product.delete()

        response = self.client.get('/products/{0}/check'.format(product.id))
        self.assertEqual(response.status_code, 404)

        response = self.client.post('/products/{0}/check'.format(product.id))
        self.assertEqual(response.status_code, 404)


    def test_product_delete(self):
        product = Product(title='ナオコ', content=u'サイトー', price=5000)
        product.save()

        response = self.client.get('/products/{0}/delete'.format(product.id))
        self.assertEqual(response.status_code, 200)

        product.delete()

        response = self.client.get('/products/{0}/delete'.format(product.id))
        self.assertEqual(response.status_code, 404)

        response = self.client.post('/products/{0}/delete'.format(product.id))
        self.assertEqual(response.status_code, 404)


    def test_product_entry(self):
        response = self.client.get('/products/entry')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/products/entry')
        self.assertEqual(response.status_code, 200)

