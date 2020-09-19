# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:33:25 2020

Materia: Programaci+on Avazada 'A'
@author: José León Alarcón
@author: Emerson Palacios Balderramo

"""
from random import randint
from functools import reduce
import pandas as pd 
import os 

class TicTacToe:
    def __init__(self):
        self.tablero = [["", "", ""],
                        ["", "", ""],
                        ["", "", ""]]
        
    
    def tableroLLeno(self):
        ####################################################################################
        ###################### USO DE FUNCIONES DE ORDEN SUPERIOR  #########################
        ####################################################################################
        lineasCasillas = map(lambda x: len(x),  list(map(lambda x: list(filter(lambda j: j != '', x)), self.tablero)))
        total = reduce(lambda x,y: x+y,lineasCasillas)
        return True if total == 9 else False
    
    def cambiaTurno(self, turnoAnterior):
        if turnoAnterior == 0: #Jugó el ordenador
            return 1
        return 0
    
    def casillaOcupada(self,  fil, col):
        if self.tablero[fil][col] != "":
            return True
        return False
    
    ####################################################################################
    ###################### IMPLEMENTACIÓN DE FUNCIÓN RECURSIVA #########################
    ####################################################################################
    def formateaTablero(self, i= 0, j = 0):
        if j == len(self.tablero):
            j = 0
            i +=1
        try:
            self.tablero[i][j] = ''
        except:
            return
        return self.formateaTablero(i, j+1)
        
    def actualizarEstadistica(self, jugador, estado):
        
        archivo = pd.read_csv('estadisticas.csv', sep=",")
        try:
            archivo.loc[archivo['Jugador'] == jugador, estado['Key']] = estado['valor']
            archivo.to_csv('estadisticas.csv',  index=None)
        except KeyError:
            print("error")
            pass
    
    def leerEstadisticas(self, jugador):
        archivo = pd.read_csv('estadisticas.csv', sep=',')
        ####################################################################################
        ###################### USO DE FUNCIONES DE ORDEN SUPERIOR  #########################
        ####################################################################################
        jugadorExiste = len(list(filter(lambda x: x == jugador, archivo['Jugador'])))
        if jugadorExiste != 0:
            #si existe 
            indice = list(archivo['Jugador']).index(jugador)
            return {
                'Jugador': archivo['Jugador'][indice], 
                'Ganadas': archivo['Ganadas'][indice], 
                'Perdidas': archivo['Perdidas'][indice], 
                'Empate': archivo['Empate'][indice]}
        nuevoJugador = {
            'Jugador': jugador,
            'Ganadas': 0,
            'Perdidas': 0, 
            'Empate': 0}
        nuevo = pd.DataFrame(columns=['Jugador', 'Ganadas', 'Perdidas', 'Empate'])
        nuevo = nuevo.append(nuevoJugador, ignore_index=True )
        nuevo.to_csv('estadisticas.csv', index=None, mode="a", header=not os.path.isfile('estadisticas.csv'))
        return nuevoJugador
        
          
    def jugadaUsuario(self, fil, col, turno):
        if not self.casillaOcupada(fil, col):
            self.tablero[fil][col] = str(turno)
            
            if self.tableroLLeno():
                return -1
            return self.tablero
        elif self.tableroLLeno():
            return -1 #
        return None
    
    def alguienGano(self, turno):
        ####################################################################################
        ###################### USO DE FUNCIONES DE ORDEN SUPERIOR  #########################
        ####################################################################################
        ganador = list(map(lambda x: list(filter(lambda j: j == turno, x)), self.tablero))
        cantidad = list(map(lambda x: len(x), ganador))
        try:
            cantidad.index(3)
            return True
        except:
            pass
        #evalua columnas 
        for i in range(0, len(self.tablero)):
            filas = 0
            for j in range(0, len(self.tablero)):
                if self.tablero[j][i] == turno:
                    filas += 1
            if filas == 3:
                return True
        #evalua diagonal principal
        diagonalp = 0
        for i in range(0, len(self.tablero)):
            if self.tablero[i][i] == turno:
                diagonalp+=1
        if diagonalp == 3:
            return True
        
        #evalua diagonal secuandaria
        diagonals = 0
        for i in range(0, len(self.tablero)):
            if self.tablero[i][len(self.tablero)-(i+1)] == turno:
                diagonals +=1
        if diagonals == 3:
            return True
        return False
            
    
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
        
        #uso de función de primera clase
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
      
        while True:
            fil = randint(0, 2)
            col = randint(0, 2)
            if not self.casillaOcupada(fil, col):
                self.tablero[fil][col] = computador 
                return fil, col, computador
     
    
        
                        
       


            
    
    
    
    

    
    