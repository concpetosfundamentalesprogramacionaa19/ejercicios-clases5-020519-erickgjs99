"""
    file: run_4.py
    autor: erickgjs99
"""
# Declaracion de variables importantes
ciclo_uni = 1200
segu_ciclo = 0
#Preguntar al usuario
edad = input("¿Cuantos años tienes? \n")
modalidad = input("Estudias en modalidad a Distancia \n 1._Si \n 2._No \n")
#Factores a determinar para el cobro
edad = int(edad) 
modalidad = int(modalidad)

#Si es de modalidad a distancia y es menor a 20 años
if (modalidad == 1 & edad <= 20):
    segu_ciclo = 100
    calc_uni = (ciclo_uni * 10)+(segu_ciclo * 10)
    print("El precio a pagar por su carrera a distancia sale un costo de $ %d" % (calc_uni),"màs seguro incluido")

#Si es de modalidad a distancia y es mayor a 20 años    
if (modalidad == 1 & edad >= 20):
    segu_ciclo_2 = 150
    calc_uni = (ciclo_uni * 10)+(segu_ciclo * 10)
    print("El precio a pagar por su carrera a distancia sale un costo de $ %d" % (calc_uni),"màs seguro incluido")

#Si es de modalidad presencial y es menor a 20 años
if (modalidad == 2 & edad <= 20):
    segu_ciclo = 100
    calc_uni = (ciclo_uni * 8)+(segu_ciclo * 8)
    print("El precio a pagar por su carrera presencial sale un costo de $ %d" % (calc_uni),"màs seguro incluido")

#Si es de modalidad presencial y es mayor a 20 años
if (modalidad == 1 & edad > 20):
    segu_ciclo_2 = 150
    calc_uni = (ciclo_uni * 8)+(segu_ciclo * 8)
    print("El precio a pagar por su carrera presencial sale un costo de $ %d" % (calc_uni),"màs seguro incluido")
