#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoohija import CalculadoraHija

def sumaN(listaops):
    op_aux = 0

    for op_n in listaops:
        result = op_aux + int(op_n)
        op_aux = result

    return result

def restaN(listaops):    
    op_aux = int(listaops[0])

    for op_n in listaops[1:]:
        result = op_aux - int(op_n)
        op_aux = result

    return result

def multN(listaops):
    op_aux = 1

    for op_n in listaops:
        result = op_aux * int(op_n)
        op_aux = result

    return result

def divideN(listaops):
    op_aux = int(listaops[0])

    for op_n in listaops[1:]:
        result = op_aux / int(op_n)
        op_aux = result

    return result

calculadorahija = CalculadoraHija()

fichero_calcs = open(sys.argv[1], 'r')
lineas = fichero_calcs.readlines()

for linea in lineas:
    elems = linea.split(',')
    elems[-1] = elems[-1][:-1] # me cargo el salto de linea de cada ultimo elemento
    operandos = elems[1:]

    if elems[0] == "suma":
        resultado = sumaN(operandos)
    elif elems[0] == "resta":
        resultado = restaN(operandos)  
    elif elems[0] == "multiplica":
        resultado = multN(operandos)  
    elif elems[0] == "divide":
        try:
            resultado = divideN(operandos)  
        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed") 
    else:
        print('Operacion no valida. Operaciones disponibles:' + 
            ' "suma", "resta", "multiplica" y "divide".')

    print(resultado) 
