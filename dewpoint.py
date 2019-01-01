#!/usr/bin/python3
####################
##Library Imports ##
####################

## Adafruit SI7021 Temp/Humidity
import board
import busio
import adafruit_si7021

#####################
## GPIO Pin Setups ##
#####################

## Adafruit SI7021 Temp/Humidity Setup
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

print ("Current Dew Point Approximation in Celcius =", (sensor.temperature -((100-sensor.relative_humidity)/5)))
