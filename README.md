# Dillon Shifts

Some resources used to create an Auction system implemented using Google app scripts and a flask backend hosted on Heroku

## Getting Started

* Start by going to [quickstart](https://developers.google.com/apps-script/api/quickstart/python) and follow all the steps, except use my quickstart.py for step 3 instead of their code.

* Click through to authenticate. The first time you run the script, it will open your browser
* Choose the Google Account that corresponds to the credentials you used to call the script
* You will get a warning **This App Isn't Verified**. Click **advanced** and **go to myapp**(myapp is the name of yourapp).
* Hit **Allow** twice and then exit out of the window.

### Next Steps With Google App Scripts
* Copy the CreateForm.js into a Google App Script
* Publish it as an api executable. [This](https://developers.google.com/apps-script/api/how-tos/execute) link has additional details if you get stuck
* You will need to set up a Google Cloud Console Platform and link your script to that platform using the Resources tab on Google App Scripts. This is described in detail in the link above but sometimes is confusing.

### Calling your App Script from Python
* Use the CreateForm.py file to call your app script from python

### Finally
* Repeat for the other two files to read responses from those forms

### To Note
* There are a lot of intermediate steps needed in between to link these. you will need to host your python scripts somewhere. I'd reccomend heroku but Google Cloud might make more sense.
* to do something on a form submit, look into installable triggers, also you can ask me if you get there
