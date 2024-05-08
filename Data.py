import serial
import time
from time import sleep

#creates "aurduino" object through wihc readings are fed to the program
arduino = serial.Serial(port = "COM3", baudrate = 57600, timeout = 0.1)

#a function to read several lines of data and gather their average
def read():
    weights = []
    last_10 = []
    for i in range(100):
        msg = arduino.readline().decode().strip()
        if msg == "":
            pass
        elif msg == None:
            pass
        else:
            weights.append(msg)
    for x in range(1,11):
        last_10.append(float(weights[len(weights) - x]))
    return round(sum(last_10)/len(last_10), 2)


