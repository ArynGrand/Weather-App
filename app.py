import requests

weatherApi = "c747625632d66c48eb6b8c7f196fbd98"

user_input = input("Enter city name: ")
weather_data= requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={weatherApi}").json()

weather = weather_data['weather'][0]['main']
temperature_kelvin = weather_data['main']['temp']

print(weather)
print(temperature_kelvin)