import tkinter as tk
from tkinter import messagebox
import requests

api_key = "686827d6e04e5220ddf15a837e3961da"

def weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

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
            messagebox.showerror("Error", "City not found or API request failed.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

window = tk.Tk()
window.title("Weather Forecast")

frame = tk.LabelFrame(window, text="Enter City", padx=20, pady=20)
frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

location_label = tk.Label(frame, text="Location:")
location_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(frame)
city_entry.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(frame, text="Search", command=display_weather)
search_button.grid(row=0, column=2, padx=10, pady=10)

result_frame = tk.LabelFrame(window, text="Weather Information", padx=20, pady=20)
result_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

temp_label = tk.Label(result_frame, text="Temperature: N/A")
temp_label.grid(row=0, column=0, padx=10, pady=10)

humidity_label = tk.Label(result_frame, text="Humidity: N/A")
humidity_label.grid(row=1, column=0, padx=10, pady=10)

wind_label = tk.Label(result_frame, text="Wind Speed: N/A")
wind_label.grid(row=2, column=0, padx=10, pady=10)

pressure_label = tk.Label(result_frame, text="Pressure: N/A")
pressure_label.grid(row=3, column=0, padx=10, pady=10)

rain_label = tk.Label(result_frame, text="Precipitation: N/A")
rain_label.grid(row=4, column=0, padx=10, pady=10)

window.mainloop()
