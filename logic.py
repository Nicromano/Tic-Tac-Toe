# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:33:25 2020

@author: NICROMANO
"""




tablero = [[" "]*3]*3
turno = 0 #0 para la maquina 1 para el jugador 


def tableroLLeno(tablero):
    casillasLlenas = 0
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero)):
            if tablero[i][j] != ' ':
                casillasLlenas = casillasLlenas+1
    return True if casillasLlenas == 9 else False

def cambiaTurno(turnoAnterior):
    if turnoAnterior == 0: #Jugó el ordenador
        return 1
    return 0

def casillaOcupada(tablero, fil, col):
    if tablero[fil][col] != " ":
        return True
    return False

def jugadaUsuario(tablero, pos, turno):
    if not casillaOcupada(tablero, pos):
        tablero[pos] = str(turno)
    return tablero


def jugadaComputador(tablero, turno):
    fila = 0
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero)):
            


print(len(tablero))
    
    
    

    
    