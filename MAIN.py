# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 00:00:19 2020

Materia: Programaci+on Avazada 'A'
@author: José León Alarcón
@author: Emerson Palacios Balderramo
"""
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.font import Font
from logic import TicTacToe
from functools import partial
import rx
from rx import operators as op

class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("TIC TAC TOE")
        self.width = 400
        self.height = 300
        self.tablero = TicTacToe() #variable para tablero
        self.parent.config(cursor='arrow')
        self.x_cordinate = int((self.parent.winfo_screenwidth()/2) - (self.width/2))
        self.y_cordinate = int((self.parent.winfo_screenheight()/2) - (self.height/2))
        self.parent.geometry('%dx%d+%d+%d' % (self.width,self.height, self.x_cordinate, self.y_cordinate))
        self.parent.resizable(False, False)
        self.parent.configure(background='beige')
        
        self.FrameCentral = tk.Frame(master=self.parent,
                    width=self.width,
                    height=self.height,
                    bg='beige')
        self.FrameCentral.grid_propagate(0)
        self.FrameCentral.config(cursor='arrow')
        self.FrameCentral.place(x=0,y=0)
        self.principal()
        
        
    def principal(self):
        ####################################################################################
        ###################### USO DE OPERADORES DE TRASNFORMACIÓN #########################
        ####################################################################################
        self.vaciarFrameReactiveX(self.FrameCentral)
        self.fuente.subscribe(lambda x: print("objeto eliminado"))
        self.CreateLabel(self.FrameCentral, "TIC TAC TOE", 50, 200, Font(family="Helvetica",size=15,weight="bold"), 'beige')
        self.CreateImage(self.FrameCentral, 'tic_128.png', 50, 75, 125, 125)
        self.nameJugador = tk.Entry(self.FrameCentral, justify=tk.CENTER, width=30)
        self.CreateButton(self.FrameCentral, 'SALIR', 200, 175, 16, 1, 'BLUE', 'WHITE', self.salirJuego)
        self.CreateButton(self.FrameCentral, 'JUGAR', 200, 125, 16, 1, 'GREEN', 'WHITE',  self.empiezaJuego)
        self.CreateLabel(self.FrameCentral, 'Ingresa nombre del jugador', 100, 10, Font(family="Helvetica",size=12,weight="bold"), 'beige')
        self.nameJugador.place(x=110, y =50)
                                
    def salirJuego(self):
        cuadro = messagebox.askyesno(message="¿Desea salir?", title="Fin del juego")
        if cuadro:
            ####################################################################################
            ###################### USO DE OPERADORES DE TRASNFORMACIÓN #########################
            ####################################################################################
            self.vaciarFrameReactiveX(self.FrameCentral)
            self.fuente.subscribe(lambda x: print("objeto eliminado"))
            self.parent.quit()
        
    def CreateLabel(self, window, text, row, col, font, bg):
        tk.Label(window,
             text= text,
             font=font, bg=bg).place(x=row, y = col)
        
    def CreateButton(self, window, text, x, y, w, h, bg, fg, action, textvar = None):
        if textvar is None:
            tk.Button(window, 
               text=text,
               command=action,
               width=w,
               height=h, 
               bg=bg, 
               fg=fg).place(x=x, y=y)
        else:
            return tk.Button(window, 
                   textvariable=textvar,
                   command=action,
                   width=w,
                   height=h, 
                   bg=bg, 
                   fg=fg).place(x=x, y=y)
    
    def CreateImage(self, window, path, x, y, width, height):
        img = Image.open(path)
        img = img.resize((width, height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(window, image = img, bg ="beige")
        panel.image=img
        panel.place(y=y, x=x)
        
        ####################################################################################
        ######### Vaciar frame con observadores y operador de transformación ###############
        ####################################################################################
    def vaciarFrameReactiveX(self, frame):
        self.fuente = rx.from_list(frame.winfo_children()).pipe(
            op.map(self.VaciarFrame))
        frame.pack_forget()
        
    def VaciarFrame(self, widget):
        widget.destroy()
        
        
    def EnviarJugadaJugador(self, fil, col):
        #print(fil, col)
        tablero_aux = self.tablero.jugadaUsuario(fil, col, self.turno)
        if tablero_aux is None:
            messagebox.showinfo(message="Casilla llena", title="Seleccione otra casilla")
        elif tablero_aux== -1:
            actualiza = {'Key':'Empate', 'valor': self.estadisticas['Empate']+1}
            self.tablero.actualizarEstadistica(self.name, actualiza)
            self.empiezaDeNuevo('Empate!!')
        else:
            self.text_jugada[fil][col].set(self.turno)
            i, j, computador= self.tablero.jugadaComputador(self.turno)
            self.text_jugada[i][j].set(computador)
            if  self.tablero.alguienGano(self.turno):
                #ganó el usuario
                messagebox.showinfo(message="Felicidades, has ganado!", title="Ganador")
                actualiza = {'Key':'Ganadas', 'valor': self.estadisticas['Ganadas']+1}
                self.tablero.actualizarEstadistica(self.name, actualiza)
                self.empiezaDeNuevo('Ganador!!')
            if  self.tablero.alguienGano(self.tablero.cambiarFicha(self.turno)):
                #ganó el computador
                messagebox.showinfo(message="Has perdido. Intentalo de nuevo", title="Perdida")
                actualiza = {'Key':'Perdidas', 'valor': self.estadisticas['Perdidas']+1}
                self.tablero.actualizarEstadistica(self.name, actualiza)
                self.empiezaDeNuevo('Perdida')
    
    def empiezaDeNuevo(self, titulo):
        respuesta = messagebox.askyesno(message="¿Desea empezar de nuevo?", title=titulo)
        self.tablero.formateaTablero()
        self.formateaTableroBotones()
        if respuesta: 
            self.empiezaJuego()
        else:
            self.principal()
            
    def formateaTableroBotones(self):
        
        for i in range(0, len(self.text_jugada)):
            for j in range(0, len(self.text_jugada)):
                self.text_jugada[i][j].set("")
        
    def FrameJugeo(self):
        self.CreateLabel(self.FrameCentral, 'Es el turno de {} con ficha: {}'.format(str(self.name) , self.turno), 100, 10, Font(family="Helvetica",size=12,weight="bold"), 'beige')
        self.tablero_botones = [[None, None, None], [None, None, None], [None, None, None]]
        self.text_jugada = [[None, None, None], [None, None, None], [None, None, None]]
        self.CreateButton(self.FrameCentral, 'Juego nuevo',200, 100, 16, 1, 'GREEN', 'WHITE', partial(self.empiezaDeNuevo, 'Juego nuevo'))
        self.CreateButton(self.FrameCentral, 'Salir', 200, 150, 16, 1, 'BLUE', 'WHITE', self.principal)
        
        ## Crear visualización de estadisticas
        
        var = tk.StringVar()
        self.estadisticas = self.tablero.leerEstadisticas(self.name)
        variablePrueba = ''
        var.set('')
        for clave, valor in self.estadisticas.items():
            variablePrueba += "%s: %s    " % (clave, valor)
        var.set(variablePrueba)
        l = tk.Label(self.FrameCentral, textvariable=var,justify=tk.LEFT, font= Font(family="Helvetica",size=10,weight="normal"), wraplength=398, bg='beige')
        l.place(x=40, y= 225)
        
        
        for i in range(0, 3):
            for j in range(0, 3):
                self.text_jugada[i][j] = tk.StringVar()
                self.text_jugada[i][j].set('') 
                self.tablero_botones[i][j] = self.CreateButton(self.FrameCentral,'', 50 + (j*45), 75 +(i*40),5, 2, 'WHITE', 'BLACK', partial(self.EnviarJugadaJugador, i, j), self.text_jugada[i][j] )
        if self.turno == 'O':
            fil, col, computador = self.tablero.jugadaComputador(self.turno)
            self.text_jugada[fil][col].set(computador)
        
        

    def empiezaJuego(self):
        try:
            self.name = self.nameJugador.get()
        except: 
            pass
        if self.name.isspace() or self.name == '':
            messagebox.showinfo(message="Ingrese nombre del jugador", title="Jugador")
            self.nameJugador.config(state=tk.NORMAL)
            self.nameJugador.delete(0, tk.END)
        else:
            ####################################################################################
            ###################### USO DE OPERADORES DE TRASNFORMACIÓN #########################
            ####################################################################################
            self.vaciarFrameReactiveX(self.FrameCentral)
            self.fuente.subscribe(lambda x: print("objeto eliminado"))
            self.turno = "X" if messagebox.askyesno(message="¿Desea empezar primero?", title="Orden de participación") else "O"
            self.FrameJugeo()
            
            

if __name__ == '__main__':
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
  
