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
    def alguienGano(self, turno):
        
        pass
    
    def intentaGanarPc(self, computador):
        
        #intenta ganar en fila
        for i in range(0, len(self.tablero)):
            fila = 0
            for j in range(0, len(self.tablero)):
                if self.tablero[i][j] == computador:
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
                if self.tablero[j][i] == computador:
                    columna += 1
            if columna == 2:
                for j in range(0, len(self.tablero)):
                    if self.tablero[j][i] == '':
                        self.tablero[j][i] = computador
                        return j, i, computador
        
        #intenta bloquear diagonales 
        #diagonal principal
        diagonalp = 0
        for i in range(0, len(self.tablero)):
            if self.tablero[i][i] == computador:
                diagonalp += 1
        if diagonalp == 2:
            for i in range(0, len(self.tablero)):
                if self.tablero[i][i]== '':
                    self.tablero[i][i] = computador
                    return i, i, computador
                    
        #diagonal secundaria 
        diagonals = 0
        for i in range(0, len(self.tablero)):
            if self.tablero[i][len(self.tablero)-(i+1)] == computador:
                diagonals +=1
        if diagonals == 2:
            for i in range(0, len(self.tablero)):
                if self.tablero[i][len(self.tablero)-(i+1)] == '':
                    self.tablero[i][len(self.tablero)-(i+1)] = computador 
                    return i, len(self.tablero)-(i+1), computador
        
        return None, None, computador
    
    ## FUNCIÓN DE PRIMERA CLASE ###
    def cambiarFicha(self, turno):
        return "O" if turno == "X" else "X"
    
    def jugadaComputador(self, turno):
        fil = None
        col = None
        
        ficha = self.cambiarFicha
        computador = ficha(turno)
        
        
        fil, col, computador = self.intentaGanarPc(computador)
        if fil != None and col != None:
            return fil, col, computador
        
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
        
        #intenta bloquear diagonales 
        #diagonal principal
        diagonalp = 0
        for i in range(0, len(self.tablero)):
            if self.tablero[i][i] == turno:
                diagonalp += 1
        if diagonalp == 2:
            for i in range(0, len(self.tablero)):
                if self.tablero[i][i]== '':
                    self.tablero[i][i] = computador
                    return i, i, computador
                    
        #diagonal secundaria 
        diagonals = 0
        for i in range(0, len(self.tablero)):
            if self.tablero[i][len(self.tablero)-(i+1)] == turno:
                diagonals +=1
        if diagonals == 2:
            for i in range(0, len(self.tablero)):
                if self.tablero[i][len(self.tablero)-(i+1)] == '':
                    self.tablero[i][len(self.tablero)-(i+1)] = computador 
                    return i, len(self.tablero)-(i+1), computador
        #juega para random
      
        print("Jugó para random")
        while True:
            fil = randint(0, 2)
            col = randint(0, 2)
            if not self.casillaOcupada(fil, col):
                self.tablero[fil][col] = computador 
                return fil, col, computador
     
        
                        
       


            
    
    
    
    

    
    