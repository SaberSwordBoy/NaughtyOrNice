print("[!] Importing Modules")
import pygame
import random
import time
import serial
import os
import subprocess
import threading
import string
pygame.init()

print("[!] Initiating Serial Connection with Arduino")
serial = serial.Serial("/dev/ttyACM0", 9600, timeout=0.1)

print("[!] Loading Sound files")
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

camerasounds1 = pygame.mixer.Sound("soundscrate-camera-sounds-various-1.wav")
camerazoom = pygame.mixer.Sound("soundscrate-camera-zoom-2.wav")
slotmachine = pygame.mixer.Sound("soundscrate-casino-slot-machine-2.wav")
powerup2 = pygame.mixer.Sound("soundscrate-scifi-weapon-power-up-mid-2.wav")
musicbox = pygame.mixer.Sound("soundscrate-christmas-music-box-1.wav")

print("[!] Sound files loaded")

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
    print("[!] Taking Picture")
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

def main():
    print("[!] Starting Main Loop")
    running = True
    button_pressed = False
    while running:
        serial_in = serial.readline()
        if not "0" in serial_in:
            print(f"[SERIAL]: {serial_in}")
        if b"naughty" in serial_in:
            print("[AUDIO] Playing Nice Voice")
            random.choice(naughtySounds).play()
        if b"nice" in serial_in:
            print("[AUDIO] Playing Naughty Voice")
            random.choice(niceSounds).play()
        if b"buildup" in serial_in:
            print("[AUDIO] Playing Buildup Sequence")
            thread = threading.Thread(target=takePicture)
            thread.start()
            powerUpSequence()
print("[!] Starting Loop")
print("""
┏━┓━┏┓━━━━━━━━━━━━━┏┓━━━┏┓━━━━━━━━━━┏━━━┓━━━━━━━┏━┓━┏┓━━━━━━━━━━━━━━┏━━┓━━━━━━━━━
┃┃┗┓┃┃━━━━━━━━━━━━━┃┃━━┏┛┗┓━━━━━━━━━┃┏━┓┃━━━━━━━┃┃┗┓┃┃━━━━━━━━━━━━━━┃┏┓┃━━━━━━━━━
┃┏┓┗┛┃┏━━┓━┏┓┏┓┏━━┓┃┗━┓┗┓┏┛┏┓━┏┓━━━━┃┃━┃┃┏━┓━━━━┃┏┓┗┛┃┏┓┏━━┓┏━━┓━━━━┃┗┛┗┓┏━━┓┏┓┏┓
┃┃┗┓┃┃┗━┓┃━┃┃┃┃┃┏┓┃┃┏┓┃━┃┃━┃┃━┃┃━━━━┃┃━┃┃┃┏┛━━━━┃┃┗┓┃┃┣┫┃┏━┛┃┏┓┃━━━━┃┏━┓┃┃┏┓┃┗╋╋┛
┃┃━┃┃┃┃┗┛┗┓┃┗┛┃┃┗┛┃┃┃┃┃━┃┗┓┃┗━┛┃━━━━┃┗━┛┃┃┃━━━━━┃┃━┃┃┃┃┃┃┗━┓┃┃━┫━━━━┃┗━┛┃┃┗┛┃┏╋╋┓
┗┛━┗━┛┗━━━┛┗━━┛┗━┓┃┗┛┗┛━┗━┛┗━┓┏┛━━━━┗━━━┛┗┛━━━━━┗┛━┗━┛┗┛┗━━┛┗━━┛━━━━┗━━━┛┗━━┛┗┛┗┛
━━━━━━━━━━━━━━━┏━┛┃━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━┗━━┛━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Version 1.0

""")

if __name__ == "__main__":
    main()
