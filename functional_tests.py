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

    def test_cv_site_exists(self):
        #The user starts by finding a link to a cv site
        self.browser.get('http://127.0.0.1:8000/cv')
        self.assertNotIn('Page not found',self.browser.title)


#The user sees a link to the cv web page

#The user clicks the link and gets redirected to the CV website
#The user is then able to see the details of the cv before them
#The user should be able to see an image of the CV holder

if __name__ == '__main__':
    unittest.main(warnings='ignore')
