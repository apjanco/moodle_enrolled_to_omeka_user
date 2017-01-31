import time
import random
import codecs
import requests
import csv

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Here we set the required login information for Moodle and Omeka
moodle_user = "USER"
moodle_pass  = "PASS"
moodle_course_id = "ID"
omeka_super_user = "USER"
omeka_pass  = "-PASS"
site_name = 'https://ds-omeka.haverford.edu/atlasofthedead' #for example, site_name = 'https://ds-omeka.haverford.edu/moodleuser'


driver = webdriver.Chrome(executable_path="/Users/ajanco/projects/chromedriver") #this is the path to chromedriver, set it for your machine

driver.get("https://moodle.haverford.edu/") # this needs to be changed for your base moodle URL

# login to Moodle
elem = driver.find_element_by_id('login_username')
elem.send_keys(moodle_user)
elem = driver.find_element_by_id('login_password')
elem.send_keys(moodle_pass)

elem.send_keys(Keys.RETURN)
time.sleep(1)

# Load the enrolled user page for the course
driver.get("https://moodle.haverford.edu/enrol/users.php?id=%s" % moodle_course_id)

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


#now we go to the Omeka project and create users for each student in the csv
login_page = str(site_name) + "/admin/users/login"
driver.get(login_page) 

#enter username
elem = driver.find_element_by_id('username')
elem.send_keys(omeka_super_user)

#enter password
elem = driver.find_element_by_id('password')
elem.send_keys(omeka_pass)

elem.send_keys(Keys.RETURN)
time.sleep(1)

#go to the users page
add_user_page = site_name + "/admin/users/add"
driver.get(add_user_page) 

#load the csv file
file_name = '/Users/ajanco/projects/students_%s.txt' % moodle_course_id
with open(file_name, 'rb') as fd:
    reader = csv.DictReader(fd)

    for row in reader:
        #enter the student username
        student_user_name = row['email'].split('@')[0]
        elem = driver.find_element_by_id('username')
        elem.send_keys(student_user_name)

        #enter display name
        student_name = row['name']
        elem = driver.find_element_by_id('name')
        elem.send_keys(student_name)

        #enter email 
        student_email = row['email']
        elem = driver.find_element_by_id('email')
        elem.send_keys(student_email)

        #select role     
        #elem = driver.find_elements_by_id('role')
        elem = driver.find_element_by_xpath("//*[@id='role']/option[@value='admin']").click()

        #press return
        elem = driver.find_element_by_id('username')
        elem.send_keys(Keys.RETURN)
        time.sleep(1)                                                 

