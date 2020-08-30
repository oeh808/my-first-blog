from django.test import TestCase
from django.urls import resolve
from .views import cv_view

# Create your tests here.

class NewVisitorTest(TestCase):

    #def decode_html():
        #W.I.P
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

    def test_contact_details_contain_the_three_headers(self):
        response = self.client.get('/cv_view/contact_details')
        html = response.content.decode('utf8')

        self.assertIn('Physical Address', html)
        self.assertIn('Telephone Number', html)
        self.assertIn('Email Address', html)

    def test_go_back_link_exists_contact(self):
        response = self.client.get('/cv_view/contact_details')
        html = response.content.decode('utf8')

        self.assertIn('Go back', html)
        self.assertIn("a href='http://127.0.0.1:8000/cv_view'", html)

    def test_cv_site_contains_a_link_to_personal_profile(self):
        response = self.client.get('/cv_view/')
        html = response.content.decode('utf8')

        self.assertIn('<a href="/cv_view/personal_profile">', html)#Check for specific link now

    def test_personal_profile_contains_header(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/personal_profile')
        html = response.content.decode('utf8')

        self.assertIn('Personal Profile', html)

    def test_personal_profile_contains_description(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/personal_profile')
        html = response.content.decode('utf8')

        self.assertIn('<p>', html)

    def test_go_back_link_exists_profile(self):
        response = self.client.get('/cv_view/personal_profile')
        html = response.content.decode('utf8')

        self.assertIn('Go back', html)
        self.assertIn("a href='http://127.0.0.1:8000/cv_view'", html)
