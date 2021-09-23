import tkinter as tk
from tkinter import *
import os
import numpy as np
import serial
import serial.tools.list_ports
import time


window = tk.Tk()
window.title("Send data to board")
window.geometry('200x150')
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


def sendDataToArduino():
    num = textBoxVal.get()
    print(type(num))
    print(num)
    value = write_read(num)
    print(value)


sendButton = tk.Button(window, text="Send", command=sendDataToArduino)
textBoxVal = tk.Entry(window, text="degree")
textBoxVal.grid(row=0, column=0)
sendButton.grid(row=1, column=0)
window.mainloop()
