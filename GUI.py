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
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

selectedPos = ""
posA = ''
posB = ''
posC = ''


def writeData(x):
    arduino.write(bytes(x, 'utf8'))
    # time.sleep(0.1)


def readArduino():
    data = arduino.readline()
    return data


def goHome():
    writeData('H')


def savePos():
    writeData("S")


def goPos():
    writeData("G")


def select(value):
    global selectedPos
    selectedPos = value


sendButton = tk.Button(window, text="Send")
textBoxVal = tk.Entry(window, text="degree")
textBoxVal.grid(row=0, column=0)
sendButton.grid(row=1, column=0)


savePosButton = tk.Button(window, text="SavePos",
                          command=savePos).grid(row=3, column=1)

goPosButton = tk.Button(window, text="GoPos",
                        command=goPos).grid(row=5, column=1)

homeButton = tk.Button(window, text="Home",
                       command=goHome).grid(row=1, column=1)

var = StringVar()
selectMenu1 = tk.Radiobutton(
    window, text="Point A", value='posA', variable=var).grid(row=2, column=0)
selectMenu2 = tk.Radiobutton(
    window, text="Point B", value='posB', variable=var).grid(row=3, column=0)
selectMenu3 = tk.Radiobutton(
    window, text="Point C", value='posC', variable=var).grid(row=4, column=0)


def waitArduino():
    global posA, posB, posC, var
    if (arduino.inWaiting()):
        resData = arduino.read_all().decode('UTF-8', errors='ignore')
        if (resData[0] == 'P'):
            print(var.get())
            selectedPos = var.get()
            if (selectedPos == ""):
                print("Chua chon pos")
            elif (selectedPos == 'posA'):
                posA = resData
            elif (selectedPos == 'posB'):
                posB = resData
            elif (selectedPos == 'posC'):
                posC = resData

        elif (resData[0] == 'H'):
            print(posA, ', ', posB, ', ', posC)
        elif (resData[0] == 'G'):
            print("go click")
    window.after(10, waitArduino)


waitArduino()
window.mainloop()
