#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
from calcoohija import CalculadoraHija

calchija = CalculadoraHija()

with open(sys.argv[1]) as fichero:

    fichero_calcs = csv.reader(fichero)

    for linea in fichero_calcs:
        operacionOK = True
        operandos = linea[1:]

        if linea[0] == "suma":
            op_aux = 0
            for operando in operandos:
                op_aux = calchija.suma(op_aux, int(operando))

        elif linea[0] == "resta":
            op_aux = int(operandos[0])
            for operando in operandos[1:]:
                op_aux = calchija.resta(op_aux, int(operando))

        elif linea[0] == "multiplica":
            op_aux = 1
            for operando in operandos:
                op_aux = calchija.mult(op_aux, int(operando))

        elif linea[0] == "divide":
            try:
                op_aux = int(operandos[0])
                for operando in operandos[1:]:
                    op_aux = calchija.divide(op_aux, int(operando))

            except ZeroDivisionError:
                sys.exit("Error: Division by zero is not allowed")
        else:
            operacionOK = False
            print('Operacion no valida. Operaciones disponibles: '
                  '"suma", "resta", "multiplica" y "divide".')

        if operacionOK is True:
            print(op_aux)  # imprime resultado para cada operacion
