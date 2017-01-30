# moodle_enrolled_to_omeka_user
This is a script that grabs a list of student names and emails from Moodle, creates a csv file and then creates users from the list on an Omeka site.

It's best to run the script on a local machince.  Clone this repo in a virtualenv and run `pip install -r requirements.txt`.<br>
You'll also need to install Chromedriver, which can be found [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

Part 1 - moodle_to_csv
  This script uses selenium to login to Moodle, navigate to the users page for a desired course and scrape the student names and emails to csv.<br>
Part 2 - csv_to_omeka
  This file reads the name and email fields from the csv, goes to your Omeka project, logs in, and creates a user account for the students on the list.<br>
Part 3 - cmoodle_enrolled_to_omeka_user.py
  This does it all.  It'll go into Moodle, gather student names and email, login to your Omeka project and create users for everyone.
