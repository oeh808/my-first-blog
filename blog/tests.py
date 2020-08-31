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

    #---------------------------------------------------------------------------

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

    #---------------------------------------------------------------------------

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

    #---------------------------------------------------------------------------

    def test_cv_site_contains_a_link_to_education(self):
        response = self.client.get('/cv_view/')
        html = response.content.decode('utf8')

        self.assertIn('<a href="/cv_view/education">', html)#Check for specific link now

    def test_education_contains_header(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/education')
        html = response.content.decode('utf8')

        self.assertIn('Education', html)

    def test_education_contains_list(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/education')
        html = response.content.decode('utf8')

        self.assertIn('<li>', html)

    def test_go_back_link_exists_education(self):
        response = self.client.get('/cv_view/education')
        html = response.content.decode('utf8')

        self.assertIn('Go back', html)
        self.assertIn("a href='http://127.0.0.1:8000/cv_view'", html)

    #---------------------------------------------------------------------------

    def test_cv_site_contains_a_link_to_work_experience(self):
        response = self.client.get('/cv_view/')
        html = response.content.decode('utf8')

        self.assertIn('<a href="/cv_view/work_experience">', html)#Check for specific link now

    def test_work_experience_contains_header(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/work_experience')
        html = response.content.decode('utf8')

        self.assertIn('Work Experience', html)

    def test_work_experience_contains_list(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/work_experience')
        html = response.content.decode('utf8')

        self.assertIn('<li>', html)

    def test_go_back_link_exists_work_experience(self):
        response = self.client.get('/cv_view/work_experience')
        html = response.content.decode('utf8')

        self.assertIn('Go back', html)
        self.assertIn("a href='http://127.0.0.1:8000/cv_view'", html)

    #---------------------------------------------------------------------------

    def test_cv_site_contains_a_link_to_interests_achievements(self):
        response = self.client.get('/cv_view/')
        html = response.content.decode('utf8')

        self.assertIn('<a href="/cv_view/interests_achievements">', html)#Check for specific link now

    def test_interests_achievements_contains_header(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/interests_achievements')
        html = response.content.decode('utf8')

        self.assertIn('Interests and Achievements', html)

    def test_interests_achievements_contains_list(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/interests_achievements')
        html = response.content.decode('utf8')

        self.assertIn('<li>', html)

    def test_go_back_link_exists_interests_achievements(self):
        response = self.client.get('/cv_view/interests_achievements')
        html = response.content.decode('utf8')

        self.assertIn('Go back', html)
        self.assertIn("a href='http://127.0.0.1:8000/cv_view'", html)

    #---------------------------------------------------------------------------

    def test_cv_site_contains_a_link_to_refrences(self):
        response = self.client.get('/cv_view/')
        html = response.content.decode('utf8')

        self.assertIn('<a href="/cv_view/refrences">', html)#Check for specific link now

    def test_refrences_contains_header(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/refrences')
        html = response.content.decode('utf8')

        self.assertIn('Refrences', html)

    def test_refrences_contains_list(self):
        response = self.client.get('http://127.0.0.1:8000/cv_view/refrences')
        html = response.content.decode('utf8')

        self.assertIn('<li>', html)

    def test_go_back_link_exists_refrences(self):
        response = self.client.get('/cv_view/refrences')
        html = response.content.decode('utf8')

        self.assertIn('Go back', html)
        self.assertIn("a href='http://127.0.0.1:8000/cv_view'", html)
