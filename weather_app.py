import requests

class Weather:
    API_KEY = "2510abb273f99c7fa3094bd2acd7530a"
    LINK = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, units = None, lang = None):
        if units is None:
            units = "metric"
        if lang is None:
            lang = "en"
        self.units = units
        self.lang = lang
        self.default_parameters = {"lang" : self.lang, "units" : self.units, "appid" : Weather.API_KEY}
    
    
    def get_info(self, *data):
        if len(data) == 1:
            if str(data[0]).isdigit():
                parameters = {"id" : data[0]}
            else:
                parameters = {"q" : data[0]}
        elif len(data) == 2:
            parameters = {"lat" : data[0], "lon" : data[1]}
        else:
            print("Wrong input")
            return

        parameters.update(self.default_parameters)
        r = requests.get(Weather.LINK, params = parameters)
        d = r.json()
        
        if r.ok:
            print("--------------------")
            print(f'Weather: {d["weather"][0]["description"]}')
            print(f'Temperature: {d["main"]["temp"]} {chr(176)}C\nPressure: {d["main"]["pressure"]}')
            print("--------------------")



x = Weather()
x.get_info("Baku City")
x.get_info(58781)
x.get_info(40.4093, 49.8671)