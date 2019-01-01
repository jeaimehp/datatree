#!/usr/bin/python3
####################
##Library Imports ##
####################

## EnviroPhat 
from envirophat import leds, motion, light, weather, analog

## Relay Shield GPIO Pins
import RPi.GPIO as GPIO

## Adafruit SI7021 Temp/Humidity
import board
import busio
import adafruit_si7021

## System Date Output and formatting
import time
import datetime

#####################
## GPIO Pin Setups ##
#####################

## Adafruit SI7021 Temp/Humidity Setup
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

## Relay shield
GPIO.setmode(GPIO.BCM)
## pins
relay1=20
relay2=19
## Mode
GPIO.setup(relay1, GPIO.OUT) 
GPIO.setup(relay2, GPIO.OUT)



## Envirophat Units
unit = 'hPa' # Pressure unit, can be either hPa (hectopascals) or Pa (pascals)

## Envirophat Analoge TMP36 Pins
cm0=0
cm5=1
cm10=2




##To Turn on Relays 
## GPIO.output(relay1, GPIO.HIGH)
## GPIO.output(relay2, GPIO.HIGH)

##Generate Ouput
point0_C=(analog.read(cm0)-.5)*100
point1_C=(analog.read(cm5)-.5)*100
point2_C=(analog.read(cm10)-.5)*100

print ('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),",",sensor.relative_humidity,",",sensor.temperature,",",light.light(),",",weather.temperature(),",",weather.pressure(unit=unit),",",point0_C,",",point1_C,",",point2_C,",",analog.read(3))
