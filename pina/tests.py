# coding=utf8

from django.test import TestCase, Client

from .models import Product

from django.db import models


class PinaStatusCodeTest(TestCase):

    # setUp は各テストメソッドの実行前に必ず実行されるメソッド
    def setUp(self):
        self.client = Client()


    # テストメソッド名は必ず test で始める
    # トップページ（インデックス）の正常表示テスト
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    # 商品一覧ページの正常表示テスト
    def test_product_list(self):
        # GET リクエストを発行
        response = self.client.get('/products')
        # レスポンスが 200 OK であるか調べる
        self.assertEqual(response.status_code, 200)


    # 商品詳細ページの表示テスト
    def test_product_detail(self):
        # 商品を登録
        product = Product(title='ナオコ', content=u'サイトー', price=3000)
        product.save()

        response = self.client.get('/products/{0}/'.format(product.id))
        # レスポンスが 200 OK であるか調べる
        self.assertEqual(response.status_code, 200)

        # 登録した商品を削除
        product.delete()

        response = self.client.get('/products/{0}/'.format(product.id))
        # レスポンスが 404 OK であるか調べる
        self.assertEqual(response.status_code, 404)


    # 商品編集ページの正常表示テスト
    def test_product_edit(self):
        product = Product(title='ナオコ', content=u'サイトー', price=5000)
        product.save()

        response = self.client.get('/products/{0}/edit'.format(product.id))
        self.assertEqual(response.status_code, 200)

        response = self.client.filter(title__startswith='ナオコ')
         

        response = self.client.post('/products/{0}/edit'.format(product.id))
        self.assertEqual(response.status_code, 302)

        product.firter        


        product.delete()

        response = self.client.get('/products/{0}/edit'.format(product.id))
        self.assertEqual(response.status_code, 404)

        response = self.client.post('/products/{0}/edit'.format(product.id))
        self.assertEqual(response.status_code, 404)


    # 商品削除ページの正常表示テスト
    def test_product_delete_check(self):
        product = Product(title='ナオコ', content=u'サイトー', price=5000)
        product.save()

        response = self.client.get('/products/{0}/check'.format(product.id))
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/products/{0}/check'.format(product.id))
        self.assertEqual(response.status_code, 302)

        # 商品を削除時の表示エラーテスト
        product.delete()

        response = self.client.get('/products/{0}/check'.format(product.id))
        self.assertEqual(response.status_code, 404)

        response = self.client.post('/products/{0}/check'.format(product.id))
        self.assertEqual(response.status_code, 404)


    # 商品削除完了の正常表示テスト
    def test_product_delete(self):
        response = self.client.get('/products/delete')
        self.assertEqual(response.status_code, 200)


    # 商品登録の正常表示テスト
    def test_product_entry(self):
        response = self.client.get('/products/entry')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/products/entry')
        self.assertEqual(response.status_code, 200)

