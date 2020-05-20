import tkinter as tk
import os
from openpyxl import Workbook
from tkinter import *
import webbrowser

wb = Workbook()

win = tk.Tk()
win.title('12school')
win.geometry('500x500')

var = IntVar()
var.set(0)

ws = wb.active

def CalendarStart():
   calendar = os.startfile('C:\schoolProgram\calendar12.bat')

def ExcelStart():
   wb.save("untitled.xlsx")

def WikiSearchFunction():
   wikisearchin = os.startfile('C:\schoolProgram\wikipediasearchw.bat')

def DnevnikOpen():
   dnevnik = os.startfile('C:\schoolProgram\dnevnik.ru-start.bat')

def change():
    if var.get() == 0:
        win['bg'] = 'red'
    elif var.get() == 1:
        win['bg'] = 'blue'
    elif var.get() == 2:
        win['bg'] = 'green'



B = Button(win, text = "Открыть календарь", command = CalendarStart)
B.place(x = 50,y = 50)

A = Button(win, text = "Сделать Excel файл", command = ExcelStart)
A.place(x = 50,y = 100)

P = Button(win, text = "Открыть онлайн энциклопедию", command = WikiSearchFunction)
P.place(x = 50,y = 150)

D = Button(win, text = "Запустить дневник.ру", command = DnevnikOpen)
D.place(x = 50,y = 200)

rad0 = Radiobutton(win, text = "Красный задний фон", variable=var, value=0, command = change)
rad0.place(x=50, y=250)

rad1 = Radiobutton(win, text = "Синий задний фон", variable=var, value=1, command = change)
rad1.place(x=50, y=300)

rad2 = Radiobutton(win, text = "Зелёный задний фон", variable=var, value=2, command = change)
rad2.place(x=50, y=350)

win.mainloop()
