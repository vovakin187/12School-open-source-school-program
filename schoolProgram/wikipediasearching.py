from tkinter.messagebox import showinfo
import wikipedia
from tkinter import *

win = Tk()
win.title('Википедия')
win.geometry('200x70')

def search_wiki() :
	search = entry.get()
	answer = wikipedia.summary(search)
	showinfo("Википедия - онлайн энциклопедия",answer)

label = Label(win,text="Поиск в Википедии :")
label.grid(row=0, column=0)

entry = Entry(win)
entry.grid(row=1,column=0)

button = Button(win,text="Найти",command=search_wiki)
button.grid(row=1,column=1,padx=10)

win.mainloop()
