import tkinter as tk
import os
from openpyxl import Workbook
from tkinter import *
import webbrowser

wb = Workbook()

win = tk.Tk()
win.title('12school')

ws = wb.active

def CalendarStart():
   calendar = os.startfile('C:\schoolProgram\calendar12.bat')

def ExcelStart():
   wb.save("untitled.xlsx")   

def WikiSearchFunction():
   wikisearchin = os.startfile('C:\schoolProgram\wikipediasearchw.bat')  

def DnevnikOpen():
   dnevnik = os.startfile('C:\schoolProgram\dnevnik.ru-start.bat')     

B = Button(win, text = "Открыть календарь", command = CalendarStart)
B.place(x = 50,y = 50)

A = Button(win, text = "Сделать Excel файл", command = ExcelStart)
A.place(x = 50,y = 100)

P = Button(win, text = "Открыть онлайн энциклопедию", command = WikiSearchFunction)
P.place(x = 50,y = 150)

D = Button(win, text = "Запустить дневник.ру", command = DnevnikOpen)
D.place(x = 50,y = 200)

win.mainloop()