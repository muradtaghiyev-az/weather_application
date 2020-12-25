## Check out this notes
```
"q" -- city`s name
"id" -- id
"lat, lon" -- coordinates
```

## Requirements

First you need to install requests module
```python
pip install requests
```

## Usage
### Create a class and input the api key and link of the website

```python
import requests

class Weather:
    API_KEY = "2510abb273f99c7fa3094bd2acd7530a"
    LINK = "https://api.openweathermap.org/data/2.5/weather"

```

## Create a function in order to define units and language
## And set default parameters (e.g. metric and english)

```python
def __init__(self, units = None, lang = None):
        if units is None:
            units = "metric"
        if lang is None:
            lang = "en"
        self.units = units
        self.lang = lang
        self.default_parameters = {"lang" : self.lang, "units" : self.units, "appid": Weather.API_KEY}

```
## Create a function and input data to get the information
```python
def get_info(self, *data):
```

## It is certain that if the length of data is 1 and data is integer
## So it is definitely id number

```python
if len(data) == 1:
            if str(data[0]).isdigit():
                parameters = {"id" : data[0]}
```
## Otherwise it is string and city`s name
```python
            else:
                parameters = {"q" : data[0]}
```
## If its length is 2, data is about coordinates
```python
elif len(data) == 2:
            parameters = {"lat" : data[0], "lon" : data[1]}
```
## If something goes wrong
```python
else:
     print("Wrong input")
     return
```
## Using "update" attribute add these parameters into default one
```python
parameters.update(self.default_parameters)
```
## Get the link
```python
r = requests.get(Weather.LINK, params = parameters)
d = r.json()
```
## If everything ok print 3 features of weather:
### 1.Description 2.Temperature  3.Pressure (chr(176) is degree symbol)
```python
if r.ok:
       print("--------------------")
       print(f'Weather: {d["weather"][0]["description"]}')
       print(f'Temperature: {d["main"]["temp"]}{chr(176)}C\nPressure: {d["main"]["pressure"]}')
       print("--------------------")
```
## Finally we input data
```python
x = Weather()
x.get_info("Baku City")
x.get_info(58781)
x.get_info(40.4093, 49.8671)
```
