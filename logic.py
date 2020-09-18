# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:33:25 2020

@author: NICROMANO
"""

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

    
    
    '''def jugadaComputador(turno):
        fila = 0
        for i in range(0, len(tablero)):
            for j in range(0, len(tablero)):'''
            
    
    
    
    

    
    