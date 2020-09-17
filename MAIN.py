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




class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("TIC TAC TOE")
        self.width = 400
        self.height = 300
        self.parent.config(cursor='arrow')
        self.x_cordinate = int((self.parent.winfo_screenwidth()/2) - (self.width/2))
        self.y_cordinate = int((self.parent.winfo_screenheight()/2) - (self.height/2))
        self.parent.geometry('%dx%d+%d+%d' % (self.width,self.height, self.x_cordinate, self.y_cordinate))
        self.parent.resizable(False, False)
        self.parent.configure(background='beige')
        
        self.CreateLabel(self.parent, "TIC TAC TOE", 50, 200, Font(family="Helvetica",size=15,weight="bold"), 'beige')
        self.CreateImage(self.parent, 'tic_128.png', 50, 75, 125, 125)
        self.nameJugador = tk.Entry(self.parent, justify=tk.CENTER, width=30)
        self.CreateButton(self.parent, 'SALIR', 200, 175, 16, 1, 'BLUE', 'WHITE', self.salirJuego)
        self.CreateButton(self.parent, 'JUGAR', 200, 125, 16, 1, 'GREEN', 'WHITE',  self.empiezaJuego)
        self.CreateLabel(self.parent, 'Ingresa nombre del jugador', 100, 10, Font(family="Helvetica",size=12,weight="bold"), 'beige')
        self.nameJugador.place(x=110, y =50)
                                    
    def salirJuego(self):
        cuadro = messagebox.askyesno(message="¿Desea salir?", title="Fin del juego")
        if cuadro:
            self.parent.quit
        return
        
    def CreateLabel(self, window, text, row, col, font, bg):
        tk.Label(window,
             text= text,
             font=font, bg=bg).place(x=row, y = col)
        
    def CreateButton(self, window, text, x, y, w, h, bg, fg, action):
        tk.Button(window, 
               text=text,
               command=action,
               width=16,
               height=1, 
               bg=bg, 
               fg=fg).place(x=x, y=y)
    
    def CreateImage(self, window, path, x, y, width, height):
        img = Image.open(path)
        img = img.resize((width, height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(window, image = img, bg ="beige")
        panel.image=img
        panel.place(y=y, x=x)
        

    
    def empiezaJuego(self):
        if self.nameJugador.get() == '' or self.nameJugador.get() == None:
            messagebox.showinfo(message="Ingrese nombre del jugador", title="Jugador")
        else:
            print("Si existe")

if __name__ == '__main__':
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
