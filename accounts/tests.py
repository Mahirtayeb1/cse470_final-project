# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AccountsViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_login_page_view(self):
        
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_page_view(self):
       
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_activate_email_view(self):
       
        token = self.user.email_token
        url = reverse('activate_email', args=[token])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
