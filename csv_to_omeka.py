#requirements
#selenium
#beautifulsoup4

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


omeka_super_user = "ajanco" #this is your omeka super user name
omeka_pass  = "-rathLar1" #password
site_name = 'https://ds-omeka.haverford.edu/atlasofthedead' #the full URL for the Omeka site
moodle_course_id = "819"


#https://ds-omeka.haverford.edu/literatureandart/admin/users/login
driver = webdriver.Chrome(executable_path="/Users/ajanco/projects/chromedriver") #this is the location of Chromedriver
login_page = str(site_name) + "/admin/users/login"
driver.get(login_page) 

#enter username
#<input type="text" name="username" id="username" value="">
elem = driver.find_element_by_id('username')
elem.send_keys(omeka_super_user)

#enter password
#<input type="password" name="password" id="password" value="">
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
                        print row['name'],row['email'] 
                    
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
                        
                        driver.get(add_user_page) 
            
    
