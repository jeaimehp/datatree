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
chordssub["temp"] = sensor.temperature
chordssub["relhumidity"] = sensor.relative_humidity

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
