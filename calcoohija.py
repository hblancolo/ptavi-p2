#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora

class CalculadoraHija(Calculadora):

    def mult(self, op1, op2):
        return op1 * op2

    def divide(self, op1, op2):
        return op1 / op2

if __name__ == "__main__":
    calculadorahija = CalculadoraHija()

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    
    if sys.argv[2] == "suma":
        resultado = calculadorahija.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = calculadorahija.resta(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        resultado = calculadorahija.mult(operando1, operando2)
    elif sys.argv[2] == "divide":
        try:
            resultado = calculadorahija.divide(operando1, operando2)
        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed")
    else:
        sys.exit('Operación sólo puede ser "suma", "resta", ' +
                 '"multiplica" o "divide".')
    print(resultado)

