import RPi.GPIO as GPIO
import serial
import time

from database import store_data 

ser = serial.Serial("/dev/ttyACMO", 9600)
ser.baudrate=9600
NODE_ID = "node_04"

def serial_com():
    read_ser = ser.readline()
    print(read_ser)
    store_data(read_ser, NODE_ID)

if __name__ == "__main__":
    while True:
        serial_com()
        time.sleep(10)
