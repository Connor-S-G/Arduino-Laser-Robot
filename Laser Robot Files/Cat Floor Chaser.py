import struct
import serial
import time
import winsound
from ctypes import windll, Structure, c_long, byref
import random

global lastXmsg
global lastYmsg

Valueerror = True
while Valueerror == True:    
    try:
        speed = int(input("Enter Speed between 1 and 10: "))
        Valueerror = False
        if speed > 10 or speed < 1:
            Valueerror = True
        
    except ValueError:
        print("OOF")
        
ser = serial.Serial('COM3', 9600, writeTimeout = 0)
xoy = 200
yoy = 100

start = int(time.perf_counter())
lastone = 0
fname= "[SOUND FILEPATH]"
sound2 = "[SOUND FILEPATH]"
sound3 = "[SOUND FILEPATH]"
sound4 = "[SOUND FILEPATH]"
sound5 = "[SOUND FILEPATH]"
sound6 = "[SOUND FILEPATH]"
sound7 = "[SOUND FILEPATH]"
sound8 = "[SOUND FILEPATH]"
sound = [fname, sound2, sound3, sound4, sound5, sound6, sound7, sound8]

if input("Press enter to start") == "":
    winsound.PlaySound(fname, winsound.SND_FILENAME)
    while True:
        whattoplay = random.randint(1,7)
        if start % 10 == 0:
            if lastone != start:
                #play random sound
                try:
                    winsound.PlaySound(sound[whattoplay], winsound.SND_FILENAME)
                except IndexError:
                    try:
                        winsound.PlaySound(sound[whattoplay+1], winsound.SND_FILENAME)
                    except IndexError:
                        winsound.PlaySound(sound[whattoplay-1], winsound.SND_FILENAME)
                lastone = int(start)
        start = int(time.perf_counter())
        yinbyte = yoy.to_bytes(1, 'little')
        xinbyte = xoy.to_bytes(1, 'little')
        ser.write(xinbyte)
        ser.write(yinbyte)

        choosey = random.randint(1,2)

            

        choosex = random.randint(1,2)
        if choosex == 1 and xoy <= 230-speed:
            xoy = random.randint(xoy, xoy+speed)
        elif choosex == 2 and xoy >= 187+speed:
            xoy = random.randint(xoy-speed, xoy)
        if choosey == 1 and yoy <= 114-speed:
            yoy = random.randint(yoy,yoy+speed)
        elif choosey == 2 and yoy >= 91+speed:
            yoy = random.randint(yoy-speed,yoy)



       
        print(choosex, xoy, choosey, yoy)



        time.sleep(0.1)
