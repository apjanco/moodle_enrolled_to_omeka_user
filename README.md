# moodle_enrolled_to_omeka_user
This is a set of scripts that grabs a list of student names and emails from Moodle, creates a csv file and then creates users from the list on an Omeka site.

It's best to run the scripts on a local machince.  Clone this repo in a virtualenv and run `pip install -r requirements.txt`.<br>
You'll also need to install Chromedriver, which can be found [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
<br>
To find the Moodle course ID, log in to Moodle, find the course and look at the URL.  You should see something like this:<br>
`https://moodle.haverford.edu/course/view.php?id=691`  The course ID is the number at the end - 691 in this case.  

Part 1 - moodle_to_csv
  This script uses selenium to log in to Moodle, navigate to the users page for a desired course and scrape the student names and emails to csv.<br>
Part 2 - csv_to_omeka
  This file reads the name and email fields from the csv, goes to your Omeka project, logs in, and creates a user account for the students on the list.<br>
