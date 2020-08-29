from selenium import webdriver
import unittest
#Here are the comments detailing how a user should use the site
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.FireFox()
    def tearDown(self):
        self.browser.quit()

    def can_see_cv_button(self):
        #The user starts by opening the main site (Blog website)
        self.browser.get('http://localhost:8000')

        self.fail('Finish the test!')
        #The user sees a link to the cv web page


        #The user clicks the link and gets redirected to the CV website
        #The user is then able to see the details of the cv before them
        #The user should be able to see an image of the CV holder

browser.quit()
