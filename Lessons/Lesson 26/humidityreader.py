import pyfirmata
import serial
import time
import plotext as plt

arduino = serial.Serial(port='/dev/tty.usbserial-14240', baudrate=9600)

def read_humidity():
    data = ""
    while len(data) < 1:
        humidity = 0
        temperature = 0
        data = arduino.readline()
        data = data.decode('utf-8')
        #if data contains hello skip
        print(data)
        if data == "Hello\r\n":
            break
        slicedata = data.split(" ")
        print(slicedata)
        humidity = (slicedata[0].split(":")[1])
        humidity = float(humidity.replace("%",""))
        print(humidity)
        temp = (slicedata[1].split(":")[1])
        temp = float(temp.replace("C",""))
        print(temp)
        return humidity, temp

    return data

graphdata = []
while True:
    graphdata = graphdata.append(read_humidity())
    print(graphdata)
    time.sleep(1)