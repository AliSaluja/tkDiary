#!/usr/bin/python3
# -*- coding: utf-8 -*-

from logic import *

del os, datetime

root = tkinter.Tk()
root.title("tkDiary")
root.resizable(width=False, height=False)
x = ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2) - 250
y = ((root.winfo_screenheight() - root.winfo_reqheight()) / 2) - 300
root.wm_geometry("300x400+%d+%d" % (x, y))

label = tkinter.Label(master=root, text="My diaryes:", height=3)
label.grid(row=0, column=0, columnspan=3)

command = lambda x="new": openWindow(key=x)
new_diary = tkinter.Button(master=root, text="New diary", command=command)
new_diary.grid(row=1, column=0)

del label, x, y, new_diary

diaryes_list = diaryes()
row = 2

if len(diaryes_list) >= 7:
    diaryes_list = diaryes()
    deletefile(diaryes_list)

for task in diaryes_list:
    command = lambda x=task: openWindow(key=x)
    tkinter.Button(master=root, text=task, command=command, width=35).grid(row=row, column=0)
    
    row += 1

del diaryes_list, row

root.mainloop()
