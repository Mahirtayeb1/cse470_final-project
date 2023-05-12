from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class HomeViewsTestCase(TestCase):
    def test_index_view(self):

        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)