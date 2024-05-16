from django.test import TestCase
from django.urls import reverse

class PollsViewsTestCase(TestCase):
    def test_index(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the polls index.")
    