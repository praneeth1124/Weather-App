import requests
import os
import pywhatkit
from datetime import datetime

user_api = "0da81aba7fcb4d5bbf2e091b88eed4e9"



complete_api_link  = "https://api.openweathermap.org/data/2.5/weather?q=Metuchen&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

lat = api_data['coord']['lat']
lon = api_data['coord']['lon']
complete_api_link2 = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&units=imperial&appid="+str(user_api)
api_link2 = requests.get(complete_api_link2)
api_data2 = api_link2.json()
#print(api_data2)
daily_max = round(api_data2['daily'][0]['temp']['max'])
daily_min = round(api_data2['daily'][0]['temp']['min'])
daily_desc= api_data2['daily'][0]['weather'][0]['description']
print(daily_max)
print(daily_min)
print(daily_desc)
#create variables to store and display data
temp_city = ((((api_data['main']['temp']) - 273.15)*9)/5 + 32)
temp_min = ((((api_data['main']['temp_min']) - 273.15)*9)/5 + 32)
temp_max = ((((api_data['main']['temp_max']) - 273.15)*9)/5 + 32)
weather_desc = str(api_data['weather'][0]['description'])
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format("Edison", date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} F".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')


if 'rain' in daily_desc:
    daily_desc= daily_desc + ". So don't forget to wear a jacket"

message = "Good Morning, Today's temperature is a Min of " + str(daily_min) + " and a Max of " + str(daily_max) + " and the weather forecast is: " + daily_desc

print(message)
pywhatkit.sendwhatmsg_to_group("EibokauzlLeApRjvTzz5sF",message,17,15)
#pywhatkit.sendwhatmsg("+18483916386",message,6,20)
#pywhatkit.sendwhatmsg("+18483916329",message,10,56)
#pywhatkit.sendwhatmsg_to_group("J9tOjAnVrdwIcbLyeX9c6k",message,6,20)

#raguma https://chat.whatsapp.com/EibokauzlLeApRjvTzz5sF
