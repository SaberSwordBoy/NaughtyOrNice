import pygame
import random
import time
import pyttsx3 as tts
import serial
import os
import subprocess
import threading
import string
pygame.init()
tts.init()

engine = tts.Engine()
engine.setProperty('rate', 125)

serial = serial.Serial("/dev/ttyACM0", 9600, timeout=0.1)

print("loaded, starting program")
naughtySounds = [
    pygame.mixer.Sound("voices/santa_hard_naughty.wav"),
    pygame.mixer.Sound("voices/santa_pile_of_coal.wav"),
    pygame.mixer.Sound("voices/santa_naughty_things.wav")
]

lenientSound = pygame.mixer.Sound("voices/santa_lenient.wav")
lenientSound.set_volume(1.0)
niceSounds = [
        pygame.mixer.Sound("voices/santa_nice_edge.wav"),
        pygame.mixer.Sound("voices/santa_very_nice.wav"),
        lenientSound,
]

calculating = [
    "Calculating you're naughty and nice score",
    "Calculating naughty or nice levels...",
    "Calculating whether you are naughty or nice..",
    "calculating naughty and nice scores"
]

camerasounds1 = pygame.mixer.Sound("soundscrate-camera-sounds-various-1.wav")
camerazoom = pygame.mixer.Sound("soundscrate-camera-zoom-2.wav")
slotmachine = pygame.mixer.Sound("soundscrate-casino-slot-machine-2.wav")
powerup2 = pygame.mixer.Sound("soundscrate-scifi-weapon-power-up-mid-2.wav")
musicbox = pygame.mixer.Sound("soundscrate-christmas-music-box-1.wav")

def powerUpSequence():
    camerazoom.play()
    musicbox.play()
    powerup2.play()
    time.sleep(camerazoom.get_length())
    camerasounds1.play()
    time.sleep(camerasounds1.get_length())
    slotmachine.play()
    time.sleep(slotmachine.get_length())

def takePicture():
    files = []
    for r, d, f in os.walk("./images", topdown=True):
        for file in f:
            files.append(file)
    name = "".join(random.choices(string.ascii_uppercase + string.digits, k=10)) + ".jpg"
    for file in files:
        if file == name:
            name == "".join(random.choices(string.ascii_uppercase + string.digits, k=10)) + ".jpg"
    output = subprocess.check_output(["fswebcam", f"images/{name}"])
    print(output)

def sayText(text):
    engine.say(text)
    engine.runAndWait()

def playResultSound(naughty):
    print(naughty)
    if naughty:
        #sayText(random.choice(naughtySounds))
        print("spoke")

    else:
        #sayText(random.choice(niceSounds))
        print("spoke")


def main():
    print("here")
    running = True
    button_pressed = False
    while running:
        serial_in = serial.readline()
        print(f"[SERIAL]: {serial_in}")
        if b"naughty" in serial_in:
            print("saying naughty text")
            random.choice(naughtySounds).play()
        if b"nice" in serial_in:
            print("saying nice text")
            random.choice(niceSounds).play()
        if b"buildup" in serial_in:
            print("playing buildup sfx")
            thread = threading.Thread(target=takePicture)
            thread.start()
            powerUpSequence()
        if b"pressed" in serial_in:
            sayText(random.choice(calculating))
print("starting....")
main()
