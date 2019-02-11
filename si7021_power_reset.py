#!/usr/bin/python3
####################
##Library Imports ##
####################


## Relay Shield GPIO Pins
import RPi.GPIO as GPIO
from time import sleep


## Relay shield
GPIO.setmode(GPIO.BCM)
## pins
#relay1=20
relay2=19
## Mode
GPIO.setwarnings(False)
#GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
##To Turn on/off Relays
##GPIO.output(relay1, GPIO.False)i
print ("Turning off BME280 - pin19")
GPIO.output(relay2, GPIO.HIGH)
print ("Giving it 10 seconds")
sleep(10)
print ("Turning back on BME280")
GPIO.output(relay2, GPIO.LOW)
