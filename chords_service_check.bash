#!/bin/bash

RESTART="/bin/systemctl restart chordspush.service"
/usr/bin/pgrep -x chordspush-rela
if [ $? -ne 0 ] # if chords not running 
then
  #reset i2c
   /home/pi/datatree/si7021_power_reset.py
  # restart chords
 $RESTART
fi
