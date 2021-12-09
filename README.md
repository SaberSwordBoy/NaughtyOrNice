# The Naughty Or Nice Box
A golden box of electronics that judges you when you press a button


# What is it?
Every year i try to make some kind of naughty or nice machine / program, and this year (2021) i made a box that does it!

Basically, it's a Raspi 0w, Arduino Uno, a breadboard, some LEDs, a bluetooth speaker, a button, and a whole bunch of wires shoved in a shoebox i spraypainted gold.
Oh yeah, and theres a camera.


# Pics
### BETTER PICTURES ARE COMING!! These are placeholders until i get better ones
(I apologize for the bad picture quality, i had to use my phone)

Here's the main box:
![Box](https://cdn.discordapp.com/attachments/892498440095928351/918554794132668457/IMG_2001.jpg)

Inside the box (no bluetooth speaker so you can see):
![Contents of the box](https://cdn.discordapp.com/attachments/892498440095928351/918554793646116945/IMG_2002.jpg)

Here's the back, pls ignore my terrible duct taping
![Back of the box](https://cdn.discordapp.com/attachments/892498440095928351/918554792819851334/IMG_2005.jpg)

# Code 
There's two code files, one for the Arduino and one for the Raspi 0w. The Raspi's code was written in python3 with vim, and essentially just plays sounds when it gets signals from the arduino, and takes a picture when nessecary.

The arduino's code does the actual naughty-or-nice deciding, and sends signals to the raspi via USB Serial. These signals are just strings, for better readability, but they could be anything, such as a single character or integers.

# Sound Effects

There's a lot of sounds in this project, most of them are the voice files that it plays to tell you if you are naughty or nice. These are in the voices folder, and were made using a website called acapela box. It's got some really cool text to speech, like the one for this, and even one that sounds like yoda! https://acapela-box.com/AcaBox/index.php

The rest of the sound effects were downloaded off of http://productioncrate.com, and played in a certain order when the raspi recieves the "buildup" command from the arduino

# Wiring 
![Picture of the arduino circuit](https://cdn.discordapp.com/attachments/892498440095928351/918544376567853106/arduino_circuit.png)
Basically, what we have here is a few LEDs wired up to the arduino with a push button for triggering the whole naughty-nice sequence.
It's not that complicated
