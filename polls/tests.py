from django.test import TestCase
from django.urls import reverse

class PollsViewsTestCase(TestCase):
    def test_index(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the polls index.")

    def test_detail(self):
        response = self.client.get(reverse('polls:detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're looking at question 1.")
    
    def test_results(self):
        response = self.client.get(reverse('polls:results', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're looking at the results of question 1.")
    
    def test_vote(self):
        response = self.client.get(reverse('polls:vote', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're voting on question 1.")
    