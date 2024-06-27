#1-Registration in OpenWeatherMap API
#2-obtain an API Key
#3-Start program
#4- if user enter city
# no -> please enter city
# yes ->send API request to the website
#  if API request successful
# no ->City not found or API request failed
# yes -> show that:
                 # Temperature in Celsius
                 # Humidity (%)
                 # Wind speed (km/h)
                 # Chances of rain (%)
                 # Pressure (hPa)

import tkinter as tk
import requests
from tkinter import messagebox

api_key = "686827d6e04e5220ddf15a837e3961da"

def weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    respons = requests.get(url)
    if respons.status_code == 200:
        return respons.json()
    else:
        print("Something went wrong!")


def display_weather():
    city = city_entry.get()
    if city:
        weather = weather_data(city)
        
        if weather:
            temp = weather['main']['temp']
            humidity = weather['main']['humidity']
            wind_speed = weather['wind']['speed']
            rain_chance = weather['clouds']['all']
            pressure = weather['main']['pressure']
            
            temp_label.config(text=f"Temperature: {temp}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind_speed} km/h")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            rain_label.config(text=f"Precipitation: {rain_chance}%")
        else:
            messagebox.showerror("Error", "City not found or API request failed!.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

window = tk.Tk()
window.title("Weather ForeCast")

location_label = tk.Label(window, text="Location:")
location_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(window)
city_entry.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(window, text="Search", command=display_weather)
search_button.grid(row=0, column=2, padx=10, pady=10)

temp_label = tk.Label(window, text="Temperature:")
temp_label.grid(row=1, column=0, padx=10, pady=10)

humidity_label = tk.Label(window, text="Humidity:")
humidity_label.grid(row=2, column=0, padx=10, pady=10)

wind_label = tk.Label(window, text="Wind Speed:")
wind_label.grid(row=3, column=0, padx=10, pady=10)

pressure_label = tk.Label(window, text="Pressure:")
pressure_label.grid(row=4, column=0, padx=10, pady=10)

rain_label = tk.Label(window, text="Precipitation:")
rain_label.grid(row=5, column=0, padx=10, pady=10)

window.mainloop()