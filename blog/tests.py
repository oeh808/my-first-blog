from django.test import TestCase
from django.urls import resolve
from .views import cv_view

# Create your tests here.

class NewVisitorTest(TestCase):

    def test_cv_view_exists(self):
        found = resolve('/cv_view/')
        self.assertEqual(found.func, cv_view)

    def test_uses_cv_view_template(self):
        response = self.client.get('/cv_view/')
        self.assertTemplateUsed(response, 'cv/cv_view.html')

    def test_cv_site_contains_a_link_to_contact_details(self):
        response = self.client.get('/cv_view/')

        html = response.content.decode('utf8')
        self.assertIn('<a href', html)
        self.assertIn('</a>', html)

        self.assertIn('<a href="/cv_view/contact_details">', html)#Check for specific link now
