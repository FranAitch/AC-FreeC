# AC/FreeC prototype
import json, requests, textmyself, time

# Set this to your location id, e.g. "2657360"
location_id = ""
# Set this to your app id (long string of numbers and letters)
app_id = ""
# Set this to the indoor temperature you don't want to exceed
indoorTemp = 23.0
# Set this to an integer like 30 (checks every half hour) or 60 (checks every hour)
# If you use some type of scheduler, leave this at None
checkInterval = None

def checkWeather():
    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}&units=metric' .format(location_id, app_id)
    response = requests.get(url)
    response.raise_for_status
    weatherData = json.loads(response.text)

    weatherGroup = weatherData['weather'][0]['id']
    mainTemp = weatherData['main']['temp']
    
    message = getText(mainTemp, weatherGroup)
    if message != None:
        textmyself.textmyself(message)
    

def getText(mainTemp, weatherGroup):
    if mainTemp >= (indoorTemp - 1):
        text = "It's {}°C outside. Time to close the windows." .format(mainTemp)
    elif str(weatherGroup).startswith('3'):
        text = "Looks like (light) rain. Take a look outside to see if you might want to close the windows."
    elif not str(weatherGroup).startswith('8') or not (int(weatherGroup) < 951 or int(weatherGroup) > 956):
        text = "Looks like unfriendly weather! Better check if you might not want to close the windows."
    else:
        text = None
    return text


def main():
    while True:
        checkWeather()
        if checkInterval:
            for i in range(checkInterval*60):
                time.sleep(1)
        else:
            break
