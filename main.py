#!/usr/bin/python3

from tkinter import *
from tkinter.scrolledtext import *
import converter


def convert():
    sqlResultText.delete('1.0',END)
    sqlResultText.insert('1.0',converter.convert(sqlQueryText.get('1.0', END), sqlInsertsEntry.get()))

top = Tk()
top.wm_title('Pega SQL Converter')
sqlQueryText = ScrolledText(top)
sqlQueryText.pack(fill=BOTH, expand=1)
sqlInsertsEntry = Entry(top)
sqlInsertsEntry.pack(fill='x')

sqlResultText = ScrolledText(top)

runButton = Button(top, text='Generate', command=convert)
runButton.pack(fill='x')
sqlResultText.pack(fill=BOTH, expand=1)

img = Image("photo", file="icon.png")
top.tk.call('wm','iconphoto',top._w,img)

top.mainloop()



