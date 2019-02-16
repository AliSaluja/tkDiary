#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import os
import tkinter

def save(filename=None, now=False):
    date = str(datetime.date.today() + datetime.timedelta(days=1)) if now == False else str(datetime.date.today())
    filename = "./src/diary/" + date + ".tkd" if filename is None else "./src/diary/" + filename + ".tkd"
    del date

    text = text_area.get("1.0",tkinter.END)

    with open(file=filename, mode="w") as outfile:
        outfile.write(text)

    del filename

def load(filename=None):
    date = str(datetime.date.today())
    filename = "./src/diary/" + date + ".tkd" if filename is None else "./src/diary/" + filename + ".tkd"
    del date

    with open(file=filename, mode="r") as text:
        result = text.read()

    del filename
    return result

def deletefile(diaryes=None):
    diaryes = diaryes[:3:-1]

    for diary in diaryes:
        patch = "./src/diary/" + diary + ".tkd"
        os.remove(patch)

    del diaryes

def diaryes():
    myDiaryes = os.listdir("./src/diary")
    myDiaryes.sort()
    myDiaryes = myDiaryes[::-1]

    myDiaryes = "".join(myDiaryes).split(".tkd")
    myDiaryes = list(filter(None, myDiaryes))

    return myDiaryes

def openWindow(key=None):
    window = tkinter.Tk()
    window.title(key)
    window.resizable(width=False, height=False)
    x = ((window.winfo_screenwidth() - window.winfo_reqwidth()) / 2) + 100
    y = ((window.winfo_screenheight() - window.winfo_reqheight()) / 2) - 300
    window.wm_geometry("500x600+%d+%d" % (x, y))

    text = "" if key == "new" else load(filename=key)
    global text_area
    text_area = tkinter.Text(master=window)
    text_area.grid(row=0, column=1)
    text_area.insert(tkinter.END, text)

    command = lambda x=False: save(now=x)
    tkinter.Button(master=window, text="Save", command=command, width=20).grid(row=1, column=1)
