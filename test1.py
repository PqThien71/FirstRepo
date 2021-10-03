import serial
import time
import codecs

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


def readArduino():
    data = arduino.readline()
    return data


while True:
    # num = input("Enter a number: ")
    # print(type(num))
    value = readArduino()
    print(value)
    str1 = value.decode('UTF-8', errors='ignore')
    print(str1[0:3])
    time.sleep(1)

    # listPulseWidth.append(value[0:3])
    # listPulseWidth.append(value[3:6])
    # listPulseWidth.append(value[6:9])
    # Sending = bytearray(listPulseWidth)
    # print(listPulseWidth)
    # print(type(listPulseWidth[2]))
    # time.sleep(1)
    # arduino.write(Sending)
