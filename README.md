# birthdays
Automatization of happy birthday's greetings  to your contacts in whatsapp 

# Needs

- python3 installed
- pywhatkit installed

# Usage

to use this code you need to download all the codes in your computer, after that you must run createjson.py to create a json file with all the dates of the years.
Now you need to fill your json file with the manage.py code, just run it and follow the instructions. Finally you need to open your WhatsApp in your default web browser and keep the saludos.py running most likely in a server.

# How it works

This project have 3 parts. Fisrt, create the empty Json file. Second, fill your Json file. Third, run saludos.py and greet everyone.
saludos.py identify the present day to look into the Json file and get who have his birthday that day. After that, this code asign a random hour to send the greeting message using Pywhatkit to open automatically you web browser and send one of two types of greeting based in the clossenes variable provided in the part 2.
This code will run forever until you stop it manually
