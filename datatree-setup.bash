#!/bin/bash
echo "Installing pip addins"
sudo pip3 install adafruit-circuitpython-si7021  


echo "Installing Envirophat"
curl -sS https://get.pimoroni.com/envirophat | bash

echo "Add OLED dir and runnign setup"
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
sudo python3 Adafruit_Python_SSD1306/setup.py install

echo "Downloading Datatree Scripts"
git clone https://github.com/jeaimehp/datatree.git
