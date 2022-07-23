"""
#########################################################################
# Weather APP using Python and OpenWeatherMap API                       #
# Copyright (C) 2022 Avino Domenico                                     #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
#########################################################################
"""

from decimal import Rounded
import json
import tkinter
import tkinter.ttk
import requests
import datetime
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("WeatherPy - Avino Domenico")
root.geometry("400x400")

root.iconbitmap("weather_few_clouds.ico")

background_image = Image.open("background.png")
background_image = background_image.resize((1920, 1080), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(background_image)
background_label = tkinter.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


mainframe = tkinter.ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

city_label = tkinter.ttk.Label(mainframe, text="City:")
city_label.grid(column=1, row=1, sticky=tkinter.W)

city_entry = tkinter.ttk.Entry(mainframe)
city_entry.grid(column=2, row=1, sticky=(tkinter.W, tkinter.E))

city_label.grid_configure(padx=10)
city_entry.grid_configure(padx=10)

search_button = tkinter.ttk.Button(mainframe, text="Search", command=lambda: get_weather(city_entry.get()))
search_button.grid(column=3, row=1, sticky=tkinter.W)

weather_label = tkinter.ttk.Label(mainframe, text="Weather:")
weather_label.grid(column=1, row=2, sticky=tkinter.W)
weather_label.grid_configure(padx=10)


def get_weather(city):
    weather_data = get_weather_from_api(city)
    weather_description = weather_data["weather"][0]["description"].capitalize()
    temperature = weather_data["main"]["temp"]
    temperature_celsius = round(temperature - 273.15, 2)
    temperature_fahrenheit = round(temperature * 9/5 - 459.67, 2)
    humidity = weather_data["main"]["humidity"]
    sunrise = weather_data["sys"]["sunrise"]
    sunset = weather_data["sys"]["sunset"]

    sunrise_time = datetime.datetime.fromtimestamp(sunrise).strftime("%H:%M:%S")
    sunset_time = datetime.datetime.fromtimestamp(sunset).strftime("%H:%M:%S")

    weather_label.configure(font=("Open Sans", 16))
    weather_label.configure(justify=tkinter.LEFT)
    weather_label.configure(text= "Weather: \n" + weather_description + "\nTemperature: " + str(temperature_celsius) + "°C / " + str(temperature_fahrenheit) + "°F\n" + "Humidity: " + str(humidity) + "%\n" + "Sunrise: " + sunrise_time + "\n" + "Sunset: " + sunset_time)

def get_weather_from_api(city):
    api_key = "7f03f0a1d9fcfcaff124b68b1d955166"
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    response = requests.get(url)
    weather_data = json.loads(response.text)
    return weather_data

root.bind('<Return>', lambda event: get_weather(city_entry.get()))

root.mainloop()