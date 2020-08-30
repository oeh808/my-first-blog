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
        self.assertIn('cv', header_text)#Working test'''

    '''def test_site_contains_contact_details(self):
        self.browser.get('http://127.0.0.1:8000/cv_view')
        #The user starts reading through the cv, seeing a link to the contact details
        contact = self.browser.find_element_by_partial_link_text('Contact Details')
        links = self.browser.find_elements_by_tag_name('a')
        self.assertIn(contact,links)

        #The user clicks the link to view the contact Details
        contact.click()

        #This then shows the user the title Contact Details as well as a header for it.
        self.assertIn('Contact Details', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Contact Details', header_text)#Working test'''

    '''def test_contact_details_visible(self):
        self.browser.get('http://127.0.0.1:8000/cv_view/contact_details')

        #The user continues to look through the website, spotting an address, a phone number and an email
        headers = self.browser.find_elements_by_tag_name('h2')

        self.assertTrue(len(headers)==3)

        self.assertIn('Physical Address', headers[0].text)
        self.assertIn('Telephone Number', headers[1].text)
        self.assertIn('Email Address', headers[2].text)'''

        #The user finds that under each header, there is some text written for the user to view.

    '''def test_information_is_valid(self):
        self.browser.get('http://127.0.0.1:8000/cv_view/contact_details')

        paragraphs = self.browser.find_elements_by_tag_name('p')

        #The user finds the Address between the address header and number headers
        self.assertTrue(type(paragraphs[0].text)==str)
        #Afterwards, the user finds the telephone number between the number header and the email header
        self.assertTrue(type(int(paragraphs[1].text))==int)
        #The user then finds the email under the email headers
        self.assertIn('@', paragraphs[2].text)'''

    def test_go_back_button(self):
        #Satisified, the user then sees a go back button and decides to press it



if __name__ == '__main__':
    unittest.main(warnings='ignore')
