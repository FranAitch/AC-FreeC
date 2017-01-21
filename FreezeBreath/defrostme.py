# Check if today is the day to defrost your freezer
import json, requests, mailMyself

location_id = None      # set to your OpenWeatherMap.org location id
app_id = None           # set to your APPID
referenceTemp = -4.0    # set to temperature below which you want ot be alerted

url = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}&units=metric' .format(location_id, app_id)
response = requests.get(url)
response.raise_for_status
weatherData = json.loads(response.text)
mainTemp = weatherData['main']['temp']

if mainTemp <= referenceTemp:
    message = 'It's {}°C outside, perfect time to defrost your freezer!' .format(mainTemp)
    mailMyself.sendMail('Defrost Me', message)
#else:
#    mailMyself.sendMail('No Defrosting Yet', 'At {}°C, it's still to warm to defrost your freezer, sorry.' .format(mainTemp)

# if you want to make sure that your getting a message, uncomment the else statement above
