##############################################
# Name: Sample Chords Submission             #
# Coded By:  Je’aime Powell                  #
# Email: jpowell@tacc.utexas.edu             #
# Created on: 1/2/2019                       #
# Revised: 1/2/2019                          #
##############################################

#Library imports
import time 
import datetime 

#Libray to post to CHoRDS
import requests

# EnviroPhat 
from envirophat import leds, motion, light, weather, analog

## Envirophat Units
unit = 'Pa' # Pressure unit, can be either hPa (hectopascals) or Pa (pascals)

## Envirophat Analog TMP36 Pins
cm0=0
cm5=1
cm10=2

##Generate Ouput
point0_C=(analog.read(cm0)-.5)*100
point1_C=(analog.read(cm5)-.5)*100
point2_C=(analog.read(cm10)-.5)*100


#Libraries for the adafruit_si7021
import board
import busio
import adafruit_si7021

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

#Needed static variables
apikey = "fajomTKKVGWxzgS7cg1o"
email = "jpowell@tacc.utexas.edu"
#url = "http://chords.tacc.cloud/about/data_urls?"
url = "http://chords.tacc.cloud/measurements/url_create?"

#Initiate Dictionary
chordssub = {"instrument_id" : 5}
chordssub = {"sensor_id" : 7}

#Add variables from sensors to dictionary
# si7021 data
chordssub["temp"] = sensor.temperature
chordssub["relhumidity"] = sensor.relative_humidity
# Envirophat data
chordssub["light"] = light.light()
chordssub["tempout"] = weather.temperature()
chordssub["pressure"] = weather.pressure(unit=unit)
chordssub["tempat0cm"] = point0_C
chordssub["tempat5cm"] = point1_C
chordssub["tempat10cm"] = point2_C

# Relay Boolean 





#Display added values
print (chordssub)

#End of URL needs
chordssub["at"] = '{:%Y-%m-%dT%H:%M:%S}'.format(datetime.datetime.now())
chordssub["email"] = email
chordssub["api_key"] = apikey


#Generate Full URL and perform request
chordsurl = requests.get(url = url,data=chordssub)

#Print response
print(chordsurl.text)
