# Author: Cameron Jones
# Description:

import urllib2
from pprint import pprint
from json import loads
import Tkinter as tk
from PIL import Image, ImageTk

class Weather:
    temp_cur = 0
    temp_max = 0
    temp_min = 0
    weather = ""
    API_URL = "http://api.openweathermap.org/data/2.1/find/name?q="

    # initializes class instance
    def __init__(self, city):
        self.city = city

    # retrieves the weather using the API
    def getWeather(self):
        data = urllib2.urlopen(self.API_URL + self.city)
        cities = loads(data.read().decode('utf-8'))
        
        # format loads weather information for multiple "cities" within requested location
        if cities['count'] > 0:
            myCity = cities['list'][0]
            
            # temperatures are sent in Kelvin and then converted to Farenheit
            self.temp_cur = ((myCity['main']['temp'] - 273.15) * 1.8) + 32
            self.temp_max = ((myCity['main']['temp_max'] - 273.15) * 1.8) + 32
            self.temp_min = ((myCity['main']['temp_min'] - 273.15) * 1.8) + 32
            self.weather  = myCity['weather'][0]['main']

    # prints the current weather (debugging purposes)
    def printWeather(self):
        print "Current Temperature: " + str(self.temp_cur)
        print "Maximum Temperature: " + str(self.temp_max)
        print "Minimum Temperature: " + str(self.temp_min)
        print "Weather: " + self.weather




bmore = Weather("baltimore")
bmore.getWeather()
bmore.printWeather()

def button_click_exit_mainloop(event):
    event.widget.quit()

root = tk.Tk()
root.title('Test')
root.bind("<Key>", button_click_exit_mainloop)

img = Image.open("mountains.jpg")
tkpi = ImageTk.PhotoImage(img)
label_img = tk.Label(root, image=tkpi).pack()
root.mainloop()
