#!/usr/bin/python3 -u
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

## Relay Shield GPIO Pins
import RPi.GPIO as GPIO

# Relay Setup
## Relay shield
GPIO.setmode(GPIO.BCM)
## pins
relay1=20 #Peltier default off
relay2=19
## Mode
GPIO.setwarnings(False)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
## Variable for relay state
#peltier = 0


# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

#Needed static variables
apikey = "fajomTKKVGWxzgS7cg1o"
email = "jpowell@tacc.utexas.edu"
#url = "http://chords.tacc.cloud/about/data_urls?"
url = "http://chords.tacc.cloud/measurements/url_create?"

#Data collection resolution
resolution = 10


while True:
  test_temp=sensor.temperature
  # Calcluate Dew Point
  dewpoint=(test_temp -((100-sensor.relative_humidity)/5))
  
  # Whether to turn on Peltier or not
  if (test_temp - dewpoint) <= 10.0 and test_temp - 10 > 1: 
    GPIO.output(relay1, GPIO.LOW)
    peltier = 1
  else:
    GPIO.output(relay1, GPIO.HIGH)
    peltier = 0
  
  #Initiate Dictionary
  chordssub = {"instrument_id" : 5}
  chordssub = {"sensor_id" : 7}
  
  #Add variables from sensors to dictionary
  # si7021 data
  chordssub["temp"] = sensor.temperature
  chordssub["relhumidity"] = sensor.relative_humidity
  chordssub["dewpoint"] = dewpoint
  chordssub["dewpointdelta"] = sensor.temperature - dewpoint
  
  # Moisture

  analog3 = analog.read(3)
  if analog3 >= 5.00:
    moisture = 0
  else:
    moisture = (1 - (analog3/ 5)) * 100

  # Envirophat data
  chordssub["light"] = light.light()
  chordssub["tempout"] = weather.temperature()
  chordssub["pressure"] = weather.pressure(unit=unit)
  chordssub["tempat0cm"] = point0_C
  chordssub["tempat5cm"] = point1_C
  chordssub["tempat10cm"] = point2_C
  chordssub["peltier"] = peltier
  chordssub["Moisture"] = moisture 
  
  
  #End of URL needs
  chordssub["at"] = '{:%Y-%m-%dT%H:%M:%S}'.format(datetime.datetime.utcnow())
  #Display added values
  print (chordssub)
  chordssub["email"] = email
  chordssub["api_key"] = apikey
  
  try: 
    #Generate Full URL and perform request
    chordsurl = requests.get(url = url,data=chordssub)
  except:
    print (chordssub["at"],"FAILED TO PUSH TO CHORDS")  
    time.sleep(15)
    continue

  #Print response
  print(chordsurl.text)
  
  #Pause between pulls
  time.sleep(resolution)
