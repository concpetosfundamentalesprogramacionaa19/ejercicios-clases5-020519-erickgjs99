"""
    file: run_3.py
    autor: @erickgjs99

"""
from misvariables import *
#uso de condicional simple 
nota = 18
nota2 = 17
nota = input("Ingrese la primera nota \n ")

nota = int(nota)

if nota >= 18:
    print("%s nota- %d" % ("Sobresaliente", nota))
else:
    if nota >= 16 & nota <= 18:
        print("%s, nota- %d" % ("Muy buena", nota))
    else:
        if nota >= 13 & nota <= 16:
            print("%s, nota- %d" % ("Regular", nota))
        else:
            print("%s, nota- %d" % ("Insuficiente", nota))

























