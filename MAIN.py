# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 00:00:19 2020

@author: NICROMANO
"""
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.font import Font


def CreateLabel(window, text, row, col, font, bg):
    tk.Label(window,
             text= text,
             font=font, bg=bg).place(x=row, y = col)
        
def CreateButton(window, text, x, y, w, h, bg, fg, action):
    tk.Button(window, 
               text=text,
               command=action,
               width=16,
               height=1, 
               bg=bg, 
               fg=fg).place(x=x, y=y)
    
def CreateImage(window, path, x, y, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image = img, bg ="beige")
    panel.image=img
    panel.place(y=y, x=x)
    
def CrearCuadroEntrada(window, x, y, w, h):
    entry = tk.Entry(window, width=w).place(x=x, y = y)
    return entry
    

def empiezaJuego(window, jugador_name):
    if jugador_name == '' or jugador_name == None:
        messagebox.showinfo(message="Ingrese nombre del jugador", title="Jugador")
    else:
        pass

    
    

def FrameInicial(window):
    CreateLabel(window, "TIC TAC TOE", 50, 200, Font(family="Helvetica",size=15,weight="bold"), 'beige')
    CreateImage(window, 'tic_128.png', 50, 75, 125, 125)
    CreateButton(window, 'SALIR', 200, 175, 16, 1, 'BLUE', 'WHITE', window.quit)
    CreateButton(window, 'JUGAR', 200, 125, 16, 1, 'GREEN', 'WHITE',  empiezaJuego)
    CreateLabel(window, 'Ingresa nombre del jugador', 100, 10, Font(family="Helvetica",size=12,weight="bold"), 'beige')
    nameJugador = CrearCuadroEntrada(window, 110, 50, 30, 10)
    

if __name__ == '__main__':
    window = tk.Tk()
    width = 400
    height = 300
    x_cordinate = int((window.winfo_screenwidth()/2) - (width/2))
    y_cordinate = int((window.winfo_screenheight()/2) - (height/2))
    window.geometry('%dx%d+%d+%d' % (width,height, x_cordinate, y_cordinate))
    window.resizable(False, False)
    window.title('Tres en Raya')
    window.configure(background='beige')
    FrameInicial(window)
    window.mainloop()
