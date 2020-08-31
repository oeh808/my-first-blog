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
        #The user starts by clicking a link to the site
        self.browser.get('http://127.0.0.1:8000/cv_view')
        self.assertNotIn('Page not found',self.browser.title)
        #The user sees the title as Omar Hussein's CV and the header as CV
        self.assertIn('Omar Hussein\'s CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CV', header_text)

    #contact Details
    #---------------------------------------------------------------------------

    def test_site_contains_contact_details(self):
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
        self.assertIn('Contact Details', header_text)

    def test_contact_details_visible(self):
        self.browser.get('http://127.0.0.1:8000/cv_view/contact_details')

        #The user continues to look through the website, spotting an address, a phone number and an email
        headers = self.browser.find_elements_by_tag_name('h2')

        self.assertTrue(len(headers)==3)

        self.assertIn('Physical Address', headers[0].text)
        self.assertIn('Telephone Number', headers[1].text)
        self.assertIn('Email Address', headers[2].text)

    def test_information_is_valid(self):
        self.browser.get('http://127.0.0.1:8000/cv_view/contact_details')

        #The user finds that under each header, there is some text written for the user to view.
        paragraphs = self.browser.find_elements_by_tag_name('p')

        #The user finds the Address between the address header and number headers
        self.assertTrue(type(paragraphs[0].text)==str)
        #Afterwards, the user finds the telephone number between the number header and the email header
        self.assertTrue(type(int(paragraphs[1].text))==int)
        #The user then finds the email under the email headers
        self.assertIn('@', paragraphs[2].text)

    def test_go_back_link_contact(self):
        #Satisified, the user then sees a go back button and decides to press it
        self.browser.get('http://127.0.0.1:8000/cv_view/contact_details')

        link = self.browser.find_element_by_partial_link_text('back')
        link.click()
        self.assertNotIn('Contact Details', self.browser.title)

    def test_site_contains_personal_profile(self):
        self.browser.get('http://127.0.0.1:8000/cv_view')
        #The user then finds a link to the personal profile
        profile = self.browser.find_element_by_partial_link_text('Personal Profile')
        links = self.browser.find_elements_by_tag_name('a')
        self.assertIn(profile,links)

        #The user clicks the link to view the contact Details
        profile.click()

        #This then shows the user the title and header; Personal Profile
        self.assertIn('Personal Profile', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Personal Profile', header_text)

    def test_go_back_link_profile(self):
        #Satisified, the user then sees a go back button and decides to press it
        self.browser.get('http://127.0.0.1:8000/cv_view/personal_profile')

        link = self.browser.find_element_by_partial_link_text('back')
        link.click()
        self.assertNotIn('Personal Profile', self.browser.title)

    #education
    #---------------------------------------------------------------------------
    def test_site_contains_education(self):
        self.browser.get('http://127.0.0.1:8000/cv_view')
        #The user then finds a link to the education page
        education = self.browser.find_element_by_partial_link_text('Education')
        links = self.browser.find_elements_by_tag_name('a')
        self.assertIn(education,links)

        #The user clicks the link
        education.click()

        #This then shows the user the title and header; Education
        self.assertIn('Education', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Education', header_text)

    def test_education_contains_lists(self):
        self.browser.get('http://127.0.0.1:8000/cv_view/education')

        #The user then sees headers with their respective lists.
        links = self.browser.find_elements_by_tag_name('h2')
        links2 = self.browser.find_elements_by_tag_name('li')

        self.assertTrue(len(links)!=0)
        self.assertTrue(len(links2)!=0)

    def test_go_back_link_education(self):
        #Satisified, the user then sees a go back button and decides to press it
        self.browser.get('http://127.0.0.1:8000/cv_view/education')

        link = self.browser.find_element_by_partial_link_text('back')
        link.click()
        self.assertNotIn('Education', self.browser.title)

    #work experience
    #---------------------------------------------------------------------------
    def test_site_contains_work_experience(self):
        self.browser.get('http://127.0.0.1:8000/cv_view')
        #The user then finds a link to the work experience page
        work = self.browser.find_element_by_partial_link_text('Work Experience')
        links = self.browser.find_elements_by_tag_name('a')
        self.assertIn(work,links)

        #The user clicks the link
        work.click()

        #This then shows the user the title and header; work experience
        self.assertIn('Work Experience', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Work Experience', header_text)

    def test_work_experience_contains_paragraph(self):
        self.browser.get('http://127.0.0.1:8000/cv_view/work_experience')

        #The user then sees headers with their respective lists.
        links = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(len(links)!=0)

    def test_go_back_link_work_experience(self):
        #Satisified, the user then sees a go back button and decides to press it
        self.browser.get('http://127.0.0.1:8000/cv_view/work_experience')

        link = self.browser.find_element_by_partial_link_text('back')
        link.click()
        self.assertNotIn('Work Experience', self.browser.title)

    #Interests and Achievements
    #---------------------------------------------------------------------------
    def test_site_contains_interests_achievements(self):
        self.browser.get('http://127.0.0.1:8000/cv_view')
        #The user then finds a link to the work experience page
        iAndA = self.browser.find_element_by_partial_link_text('Interests and Achievements')
        links = self.browser.find_elements_by_tag_name('a')
        self.assertIn(iAndA,links)

        #The user clicks the link
        iAndA.click()

        #This then shows the user the title and header; work experience
        self.assertIn('Interests and Achievements', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Interests and Achievements', header_text)

    def test_interests_achievements_contains_list(self):
        self.browser.get('http://127.0.0.1:8000/cv_view/interests_achievements')

        #The user then sees headers with their respective lists.
        links = self.browser.find_elements_by_tag_name('ul')
        links2 = self.browser.find_elements_by_tag_name('h2')

        self.assertEqual('Interests', links2[0].text)
        self.assertEqual('Achievements', links2[1].text)

        self.assertTrue(len(links)!=0)

    def test_go_back_link_interests_achievements(self):
        #Satisified, the user then sees a go back button and decides to press it
        self.browser.get('http://127.0.0.1:8000/cv_view/interests_achievements')

        link = self.browser.find_element_by_partial_link_text('back')
        link.click()
        self.assertNotIn('Interests and Achievements', self.browser.title)

    #refrences
    #---------------------------------------------------------------------------
    def test_site_contains_refrences(self):
        self.browser.get('http://127.0.0.1:8000/cv_view')
        #The user then finds a link to the work experience page
        ref = self.browser.find_element_by_partial_link_text('Refrences')
        links = self.browser.find_elements_by_tag_name('a')
        self.assertIn(ref,links)

        #The user clicks the link
        ref.click()

        #This then shows the user the title and header; work experience
        self.assertIn('Refrences', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Refrences', header_text)

    def test_refrences_contains_list(self):
        self.browser.get('http://127.0.0.1:8000/cv_view/refrences')

        #The user then sees headers with their respective lists.
        links = self.browser.find_elements_by_tag_name('ul')
        links2 = self.browser.find_elements_by_tag_name('h2')

        self.assertEqual('Contacts', links2[0].text)
        self.assertTrue(len(links)!=0)

    def test_go_back_link_refrences(self):
        #Satisified, the user then sees a go back button and decides to press it
        self.browser.get('http://127.0.0.1:8000/cv_view/refrences')

        link = self.browser.find_element_by_partial_link_text('back')
        link.click()
        self.assertNotIn('Interests and Achievements', self.browser.title)

    #---------------------------------------------------------------------------
    


if __name__ == '__main__':
    unittest.main(warnings='ignore')
