# AC/FreeC prototype
import json, requests, textmyself

# Set this to your location id, e.g. "2657360"
location_id = None

# Set this to your app id (long string of numbers and letters)
app_id = None

# Set this to the indoor temperature you don't want to exceed
indoorTemp = 20.0


url = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}&units=metric' .format(location_id, app_id)
response = requests.get(url)
response.raise_for_status
weatherData = json.loads(response.text)

weatherGroup = weatherData['weather'][0]['id']
mainTemp = weatherData['main']['temp']


def getText():
    if mainTemp >= (indoorTemp - 1):
        text = "It's {}°C outside. Time to close the windows." .format(mainTemp)
    elif str(weatherGroup).startswith('3'):
        text = "Looks like (light) rain. Take a look outside to see if you might want to close the windows."
    elif not str(weatherGroup).startswith('8') or not (int(weatherGroup) < 951 or int(weatherGroup) > 956):
        text = "Looks like unfriendly weather! Better check if you might not want to close the windows."
    else:
        text = None
    return text


message = getText()
if message != None:
    textmyself.textmyself(message)

