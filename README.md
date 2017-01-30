# moodle_enrolled_to_omeka_user
This is a script that grabs a list of student names and emails from Moodle, creates a csv file and then creates users from the list on an Omeka site.

Part 1 - moodle_to_csv
  This script uses selenium to login to Moodle, navigate to the users page for a desired course and scrape the student names and emails to csv.<br>
Part 2 - csv_to_omeka
  This file reads the name and email fields from the csv, goes to your Omeka project, logs in, and creates a user account for the students on the list.<br>
Part 3 - combined script 
  coming soon...
