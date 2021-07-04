# Vaccine appointment SMS notifier

Sends SMS when a suitable vaccine date has been found

### Description
In Belgium, we need to register our Covid-19 vaccination via https://www.laatjevaccineren.be/registratie

If you want to get a different appointment date than the one already assigned to you, you need to keep checking on a regular basis what times and dates are available. 

This is obviously time-consuming. Hence I wrote this script which checks between a given period of days if there are any slots available and sends a SMS using Twilio to your phone number.

### Pre-requisites
- Twilio account with a phone number
- Install Twilio python libraries

### How to install
- Clone the repo
- Create a config.py file with the following variables and your own values.
- Create a cron job to run the script.

### config.py

```python
# These values have be to extracted from laatejevaccineren.be/registratie
uniqueId = ""
afspraakId = ""

# The dates for which you would like to know available timeslots.
afspraakTot = "2021-07-18"
dateList = ["2021-07-13","2021-07-14","2021-07-15","2021-07-16","2021-07-17","2021-07-18"]

# Twilio account SID and auth token
twilioAuthSId = ""
twilioAuthToken = ""

# Phone numbers to send the SMS from and to
fromNumber = ""
toNumber = ""

# Log file path to write logs after every run
logFilePath = ""
```

