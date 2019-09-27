from twilio.rest import Client
import requests


# Openweathermap API key
api_key = "ADD API KEY HERE"

# base_url variable to store url to openweathermap
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# variable to store city name
city_name = "san antonio, US"

# complete_url variable to store complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into python format data
x = response.json()

# Twilio account sid
account_sid = 'ACfbb7c7388c2ca58e49d1a738c1202132'

# Twilio auth token
auth_token = 'a7c509fc37fcb15e5078504077d82c71'

# sets client variable with above variable
client = Client(account_sid, auth_token)

# if city is not found, print city not found
if x["cod"] != "404":

    # store the value of "main" key in variable y
    y = x["main"]

    # store the value corresponding to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding to the "humidity" key of y
    current_humidiy = y["humidity"]

    # store the value of "weather" key in variable z
    z = x["weather"]

    # store the value corresponding to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    temp_F = int(current_temperature)
    temp_F = ((9/5)*(temp_F - 273)) + 32
    print(temp_F)

    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")


# sets the string that should be sent by twilio
weather_text = ("Date = 01/01/2001" + "\nTemperature (F) = " + str(temp_F) +
                "\nDescription = " + weather_description)

# prints weather_text string to verify it is correct before sending
print(weather_text)

# # creates a message to send from twilio
# message = client.messages \
#                 .create(
#                      body="\n"+weather_text,
#                      from_='+FROM #',
#                      to='+TO #'
#                  )
#
# # prints the message sid for verification
# print(message.sid)