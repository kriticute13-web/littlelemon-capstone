from django.test import TestCase
from rest_framework.test import APIClient
from .models import Menu

class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            title="Burger",
            price=120.00,
            inventory=50
        )

    def test_getall(self):
        client = APIClient()
        response = client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)