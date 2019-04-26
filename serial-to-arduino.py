import time
import serial

port = "/dev/ttyACM0"
baudrate = 9600

s = serial.Serial(port,baudrate)

s.write("2")
