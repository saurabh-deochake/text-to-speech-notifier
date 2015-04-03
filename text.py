import pyttsx
import requests
import json
import re
from bs4 import BeautifulSoup

liveXMLUrl = "http://api.openweathermap.org/data/2.5/weather?q=Pune"
dataFromXMLUrl = requests.get(liveXMLUrl)

#content = {"coord":{"lon":73.86,"lat":18.52},"sys":{"message":0.0394,"country":"IN","sunrise":1427936267,"sunset":1427980710},"weather":[{"id":800,"main":"Clear","description":"Sky is Clear","icon":"01d"}],"base":"stations","main":{"temp":308.936,"temp_min":308.936,"temp_max":308.936,"pressure":951.3,"sea_level":1020.69,"grnd_level":951.3,"humidity":25},"wind":{"speed":3.11,"deg":278.5},"clouds":{"all":0},"dt":1427969112,"id":1259229,"name":"Pune","cod":200}
parse = json.loads(dataFromXMLUrl.text)

city = parse['name']
weather = parse['weather'][0]['description']
temp = round(parse['main']['temp'] - 273.15, 2)



weather = "Hello, Saurabh! The weather of",city,"is:  ",weather, "with temperature",temp,"degrees celcius"
engine = pyttsx.init()
engine.say(weather)
engine.runAndWait()

