"""
    file: run_2.py
    autor: @erickgjs99

"""
from misvariables import *
#uso de condicional simple 
nota = 18
nota2 = 17
nota = input("Ingrese la primera nota \n ")
nota2 = input("Ingrese la segunda nota \n ")

nota = int(nota)
nota2 = int(nota2)

if nota >= 18:
    print("%s, su valor de nota  es %d" % (mensaje, nota))
else:
    print("%s, su valor de nota  es %d" % (mensaje_2, nota))

if nota2 >= 18:
    print("%s, su valor de nota  es %d" % (mensaje, nota2))
else:
    print("%s, su valor de nota  es %d" % (mensaje_2, nota2))





















