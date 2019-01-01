#!/usr/bin/python3
####################
##Library Imports ##
####################


## Relay Shield GPIO Pins
import RPi.GPIO as GPIO

## Relay shield
GPIO.setmode(GPIO.BCM)
## pins
relay1=20
relay2=19
## Mode
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)

##To Turn on/off Relays
##GPIO.output(relay1, GPIO.False)
 GPIO.output(relay2, GPIO.True)
