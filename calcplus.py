#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoohija import CalculadoraHija

calculadorahija = CalculadoraHija()

fichero_calcs = open(sys.argv[1], 'r')
lineas = fichero_calcs.readlines()

for linea in lineas:
    operacionOK = True
    elems = linea.split(',')
    # me cargo el salto de linea de cada ultimo elemento
    elems[-1] = elems[-1][:-1]
    operandos = elems[1:]

    if elems[0] == "suma":
        op_aux = 0
        for operando in operandos:
            op_aux = calculadorahija.suma(op_aux, int(operando))

    elif elems[0] == "resta":
        op_aux = int(operandos[0])
        for operando in operandos[1:]:
            op_aux = calculadorahija.resta(op_aux, int(operando))

    elif elems[0] == "multiplica":
        op_aux = 1
        for operando in operandos:
            op_aux = calculadorahija.mult(op_aux, int(operando))

    elif elems[0] == "divide":
        try:
            op_aux = int(operandos[0])
            for operando in operandos[1:]:
                op_aux = calculadorahija.divide(op_aux, int(operando))

        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed")
    else:
        operacionOK = False
        print('Operacion no valida. Operaciones disponibles: "suma", '
              '"resta", "multiplica" y "divide".')

    if operacionOK is True:
        print(op_aux)  # imprime resultado para cada operacion

fichero_calcs.close()
