import requests


class WeatherData:

    def __init__(self, api_key, city_name):
        # open weather API key
        self.api_key = api_key

        # city name for weather location
        self.city_name = city_name

    def get_weather_data(self):
        print("\n===================== DEBUG INFO =====================")
        print("\tCity name = " + self.city_name)
        print("\tAPI key = " + self.api_key)
        print("======================================================")


        # base_url variable to store url to openweathermap
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # complete_url variable to store complete url address
        complete_url = base_url + "appid=" + self.api_key + "&q=" + self.city_name

        # get method of requests module return response object
        response = requests.get(complete_url)

        # json method of response object
        # convert json format data into python format data
        weather_json = response.json()

        # if city is not found, print city not found
        if weather_json["cod"] != "404":

            # store the value of "main" key in variable store_json
            store_json = weather_json["main"]

            # store the value corresponding to the "temp" key of store_json
            current_temperature = store_json["temp"]

            # store the value corresponding to the "pressure" key of store_json
            current_pressure = store_json["pressure"]

            # store the value corresponding to the "humidity" key of store_json
            current_humidiy = store_json["humidity"]

            # store the value of "weather" key in variable z
            z = weather_json["weather"]

            # store the value corresponding to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            temp_f = int(current_temperature)
            temp_f = ((9 / 5) * (temp_f - 273)) + 32
            print("\n Temperature in F = " + str(temp_f))

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


# Openweathermap API key
api_key = "ADD API KEY HERE"

w1 = WeatherData(api_key, "San Antonio, US")
w1.get_weather_data()
