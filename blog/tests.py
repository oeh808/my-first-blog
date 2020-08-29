from django.test import TestCase
from django.urls import resolve
from .views import cv_view

# Create your tests here.

class NewVisitorTest(TestCase):

    def test_cv_view_exists(self):
        found = resolve('/cv_view/')
        self.assertEqual(found.func, cv_view)
