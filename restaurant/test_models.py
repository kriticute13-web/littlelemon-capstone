from django.test import TestCase
from .models import Menu

class MenuModelTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(
            title="Ice Cream",
            price=80.00,
            inventory=100
        )

        self.assertEqual(str(item), item.title)