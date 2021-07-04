import http.client
from datetime import datetime
import json
import config
from twilio.rest import Client

conn = http.client.HTTPSConnection("covidvaccin.doclr.be")
payload = ''
headers = {
  'Host': 'covidvaccin.doclr.be',
  'Referer': 'https://covidvaccin.doclr.be/nekkerhal/patient',
  'D-Session-Token': 'PaukeslagBoem',
  'DNT': '1'
}

today = datetime.today().strftime('%Y-%m-%d')
afspraakVanaf = today
availableDates = []

for eachDate in config.dateList:
  httpQuery = "/api/public/praktijk/{}/afspraakmogelijkheden?afspraakTot={}&afspraakTypeIds={}&afspraakVanaf={}&dagTot={}&dagVan={}". \
                  format(config.uniqueId, config.afspraakTot, config.afspraakId, afspraakVanaf, eachDate, eachDate)
  conn.request("GET", httpQuery, payload, headers)
  res = conn.getresponse()
  parsed = json.loads(res.read())
  events = parsed[0]['dagen'][0]['events']
  if not events:
    print("no available time")
  else:
    availableDates.append(eachDate)

strAvailableDates = str(availableDates)
print (strAvailableDates)

messageId = ""
if len(availableDates) != 0:
    client = Client(config.twilioAuthSId, config.twilioAuthToken)
    message = client.messages \
                    .create(
                        body=strAvailableDates,
                        from_=config.fromNumber,
                        to=config.toNumber
                    )
    messageId = message.sid

# Write output to the log file
with open(config.logFilePath, 'a') as f:
    f.write("\n******************************************************************")
    now = datetime.now()
    f.write("\n"+ now.strftime)
    f.write("\n"+ strAvailableDates)
    f.write("\n"+ messageId)