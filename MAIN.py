# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 00:00:19 2020

@author: NICROMANO
"""
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image

        
def CreateLabel(window, text, row, col, padX, padY):
    ttk.Label(window, text= text).place(x=row, y = col)
        
def CreateButton(window, text, row, col, padX, padY, action):
    ttk.Button(window, text=text, command=action).place(x=row, y=col)
    
def CreateImage(window, path, col, row, padX, padY, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image = img)
    panel.image=img
    panel.grid(column=col, row=row)
    
window = tk.Tk()
background_image =ImageTk.PhotoImage(Image.open('fondo.jpg'))
background_label = ttk.Label(window, image=background_image, background='grey')
background_label.pack()
x_cordinate = int((window.winfo_screenwidth()/2) - (background_image.width()/2))
y_cordinate = int((window.winfo_screenheight()/2) - (background_image.height()/2))
window.geometry('%dx%d+%d+%d' % (background_image.width(),background_image.height(), x_cordinate, y_cordinate))
window.resizable(False, False)
window.wm_attributes('-transparentcolor','grey')
window.title('Tres en Raya')
    
CreateLabel(window, "Holaaaa", 20, 20, 20, 20)
CreateButton(window, 'Salir', 50, 40, 0, 0, window.quit)

window.mainloop()
