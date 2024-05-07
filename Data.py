import serial
import time
from time import sleep

weight_list = []


def read(comport, baudrate, switch):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while switch == True:

        data = ser.readline().decode().strip()
        if data:
            weight_list.append(data)
            sleep(5)
        if switch == False:
            break


if __name__ == '__main__':

    read('COM28', 115200)