#Converts Mouse position to bytes for X and Y servos.
import struct
import serial
import time
from ctypes import windll, Structure, c_long, byref

ser = serial.Serial('COM3', 9600)
global lastXmsg
global lastYmsg
lastXmsg = 0
lastYmsg = 0
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
    
def queryMousePosition():
    global xindegrees
    global yindegrees
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    xindegrees = int(pt.x / 15) + 128
    yindegrees = int(pt.y / 8.4375)
    return xindegrees, yindegrees
lastxmsg = 0
lastymsg = 0

if input("Press enter to start") == "":    
    while True:
        queryMousePosition()
        if xindegrees > 221:
            xindegrees = 221
        elif xindegrees < 184:
            xindegrees = 184
        if yindegrees > 71:
            yindegrees = 71
        elif yindegrees < 43:
            yindegrees = 43
        yinbyte = yindegrees.to_bytes(1, 'little')
        xinbyte = xindegrees.to_bytes(1, 'little')

        if lastXmsg != xindegrees or lastYmsg != yindegrees:
            print(xindegrees, yindegrees)
            ser.write(xinbyte)
            ser.write(yinbyte)
            lastXmsg = xindegrees
            lastYmsg = yindegrees

        time.sleep(0.01)
