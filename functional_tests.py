from selenium import webdriver
import unittest
from django.template.loader import render_to_string
from selenium.webdriver.common.keys import Keys
import time
#Here are the comments detailing how a user should use the site

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    '''def test_cv_site_exists(self):
        #The user starts by clicking a link to the site
        self.browser.get('http://127.0.0.1:8000/cv_view')
        self.assertNotIn('Page not found',self.browser.title)
        #The user sees the title as Omar Hussein's CV and the header as CV
        self.assertIn('Omar Hussein\'s CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('cv', header_text)'''#Working test

    def test_site_contains_contact_details(self):
        self.browser.get('http://127.0.0.1:8000/cv_view')
        #The user starts reading through the cv, seeing a link to the contact details
        contact = self.browser.find_element_by_partial_link_text('Contact Details')
        links = self.browser.find_elements_by_tag_name('a')
        self.assertIn(contact,links)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
