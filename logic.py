# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:33:25 2020

@author: NICROMANO
"""
from random import randint

class TicTacToe:
    def __init__(self):
        self.tablero = [["", "", ""],["", "", ""],["", "", ""]]
        
    
    def tableroLLeno(self):
        casillasLlenas = 0
        for i in range(0, len(self.tablero)):
            for j in range(0, len(self.tablero)):
                if self.tablero[i][j] != '':
                    casillasLlenas = casillasLlenas+1
        return True if casillasLlenas == 9 else False
    
    def cambiaTurno(self, turnoAnterior):
        if turnoAnterior == 0: #Jugó el ordenador
            return 1
        return 0
    
    def casillaOcupada(self,  fil, col):
        if self.tablero[fil][col] != "":
            return True
        return False
    
    
    def formateaTablero(self):
        for i in range(0, len(self.tablero)):
            for j in range(0, len(self.tablero)):
                self.tablero[i][j] = ''
        
        
    def jugadaUsuario(self, fil, col, turno):

        if not self.casillaOcupada(fil, col):
            self.tablero[fil][col] = str(turno)
            print(self.tablero)
            if self.tableroLLeno():
                return -1
            return self.tablero
        elif self.tableroLLeno():
            return -1 #
        return None
    
    def jugadaComputador(self, turno):
        fil = None
        col = None
        computador = "O" if turno == "X" else "X"
        #analiza filas y columnas
        
        #intenta bloquear fila
        for i in range(0, len(self.tablero)):
            fila = 0
            for j in range(0, len(self.tablero)):
                if self.tablero[i][j] == turno:
                    fila += 1
            if fila == 2:
                #bloquea la fila 
                for j in range(0, len(self.tablero)):
                    if self.tablero[i][j] == '':
                        self.tablero[i][j] = computador
                        return i, j, computador
        
        #intenta bloquear columnas 
        for i in range(0, len(self.tablero)):
            columna = 0
            for j in range(0, len(self.tablero)):
                if self.tablero[j][i] == turno:
                    columna += 1
            if columna == 2:
                for j in range(0, len(self.tablero)):
                    if self.tablero[j][i] == '':
                        self.tablero[j][i] = computador
                        return j, i, computador
                
        '''for i in range(0, len(self.tablero)):
            contadorfilas = 0
            contadorCol = 0
            for j in range(0, len(self.tablero)):
                if self.tablero[j][i] == turno or self.tablero[j][i] != '':
                    contadorCol += 1
                        
                if self.tablero[i][j] == turno or self.tablero[i][j] != '':
                    contadorfilas += 1
            if contadorfilas == 2:
                f = i
                break
            if contadorCol == 2:
                f = i
                break
        if contadorfilas == 2:
            print("Intenta bloquear fila")
            for y in range(0, len(self.tablero)):
                if self.tablero[f][y] != turno and self.tablero[f][y] == '':
                    self.tablero[f][y] = computador
                    fil = f
                    col = y
                    return fil, col, computador
        if contadorCol == 2:
            print("Intenta bloquear columna")
            for x in range(0, len(self.tablero)):
                    if self.tablero[x][f] != turno and self.tablero[x][f] == '':
                        self.tablero[x][f] = computador
                        fil = x
                        col = f
                        return fil, col, computador'''
        
                        
        print("Jugó para random")
        while True:
            fil = randint(0, 2)
            col = randint(0, 2)
            if not self.casillaOcupada(fil, col):
                self.tablero[fil][col] = computador 
                return fil, col, computador
   
        
                        
       


            
    
    
    
    

    
    