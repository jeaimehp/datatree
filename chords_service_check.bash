#!/bin/bash

RESTART="/bin/systemctl restart chordspush.service"
/usr/bin/pgrep -x chordspush-rela
if [ $? -ne 0 ] # if chords not running 
then
 # restart chords
 $RESTART
fi
