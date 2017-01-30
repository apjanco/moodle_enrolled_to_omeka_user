import time
import random
import codecs
import requests
import csv

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


moodle_user = "USERNAME" #this is your Moodle username
moodle_pass  = "PASSWORD" #this is your Moodle password
moodle_course_id = "ID" #this is the id that appears in the URL of your class ...php?id=691 for example

driver = webdriver.Chrome(executable_path="PATH") #this is the path to cromedriver, get from https://sites.google.com/a/chromium.org/chromedriver/downloads

driver.get("https://moodle.haverford.edu/") #change as relevant to your moodle site's URL

# login to Moodle
elem = driver.find_element_by_id('login_username')
elem.send_keys(moodle_user)
elem = driver.find_element_by_id('login_password')
elem.send_keys(moodle_pass)

elem.send_keys(Keys.RETURN)
time.sleep(1)

# Load the enrolled user page for the course
driver.get("https://moodle.haverford.edu/enrol/users.php?id=%s" % moodle_course_id) #here you may need to change URL given your site

#Now we'll pass the page's HTML to BeautifulSoup, parse it and return values for student names and emails.
html_content = driver.page_source

html_doc     = BeautifulSoup(html_content, 'html.parser')
student_names = html_doc.findAll("div", { "class" : "subfield_userfullnamedisplay" })
student_emails = html_doc.findAll("div", { "class" : "subfield_email" })
combined = zip(student_names,student_emails)  

#this section creates a csv file for the students' names and emails
file_name = '/Users/ajanco/projects/students_%s.txt' % moodle_course_id
with open(file_name, 'wb') as fd:

    field_names = ['name','email']

    writer = csv.DictWriter(fd,field_names)

    writer.writeheader()

    for name in combined:

        row = {}
        row['name']  = name[0].getText()
        row['email'] = name[1].getText()

        writer.writerow(row)
        
# close the browser
driver.quit()
