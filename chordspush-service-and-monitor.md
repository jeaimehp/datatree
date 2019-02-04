# Method to add Chordspush as a service/daemon in systemctl and monitor the service
## Chords Push Unit Code 
<pre>
pi@datatree:~/datatree $ cat chordspush.service
[Unit]
Description=Simplified simple Chordspush service
After=syslog.target
[Service]
Type=simple
User=pi
Group=pi
WorkingDirectory=/home/pi/datatree
ExecStart=/home/pi/datatree/chordspush-relay-service.py
StandardOutput=syslog
StandardError=syslog
[Install]
WantedBy=multi-user.target
</pre>

## Setting up the file
<pre>
chmod +x chordspush.service
sudo ln -s /home/pi/datatree/chordspush.service  /etc/systemd/system/
sudo systemctl enable chordspush.service
</pre>

## Check status:
<pre>
systemctl status chordspush.service
Restart:
sudo systemctl status chordspush.service
When running find out the real name of the service for pgrep (other wise will always find a process for the the actual grep)
Find the process id then
cat /proc/id/comm
</pre>

### Ex.

<pre>
pi@datatree:~/datatree $ pgrep chords
2648 #<--—Wrong one
pi@datatree:~/datatree $ ps -elf|grep chords
4 S pi        2648     1 11  80   0 -  6954 poll_s 15:13 ?        00:00:02 /usr/bin/python3 -u /home/pi/datatree/chordspush-relay-service.py
0 S pi        2664 30636  0  80   0 -  1094 pipe_w 15:13 pts/0    00:00:00 grep --color=auto chords
pi@datatree:~/datatree $ cat /proc/2648/co
comm             coredump_filter
pi@datatree:~/datatree $ cat /proc/2648/comm
chordspush-rela
</pre>


## Crontab
<pre>
pi@datatree:~/datatree $ cat chords_service_check.bash
#!/bin/bash
RESTART="/bin/systemctl restart chordspush.service"
/usr/bin/pgrep -x chordspush-rela
if [ $? -ne 0 ] # if chords not running
then
 # restart chords
 $RESTART
fi
</pre>
