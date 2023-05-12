from django.test import TestCase
from django.urls import reverse, resolve
from products.views import get_product
from .models import *
from faker import Faker
fake = Faker()

# Create your tests here.

class FirstTestCase(TestCase):
    def setUp(self):
        print('setup called')

    def test_equal(self):
        self.assertEqual(1, 1)

    #def test_get_product_urls(self):

    def test_product_models(self):
        categories = ['abc', 'def']
        for product in categories:
            obj = Product.objects.create(
                product_name = product

            )
            self.assertEquals(product, obj.product_name)

        objs = Product.objects.all()
        self.assertEqual(objs.count(), 2)