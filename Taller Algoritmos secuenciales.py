# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 23:42:12 2021

@author: ricar
"""

# Taller de ejercicios secuenciales 
# Inteligencia Computacional

#Calcule el valor de Y indicando paso a paso como llegó al resultado 
# 1. y = ( (5+2-5)^2 * 5+8/2 -30 ) / 2 * 5 -3

print("Calcular y = ( (5+2-5)^2 * 5+8/2 -30 ) / 2 * 5 -3" + "\n")
pasouno = (5+2-5)**2
pasodos = pasouno * 5+8/2-30
final = pasodos / 2 * 5 - 3
print("Primer paso: (5+2-5)**2 = ",pasouno)
print("Segundo paso: ( (5+2-5)^2 * 5+8/2 -30 ) = ",pasodos)
print("Resultado final = ", final)
print("")

# 2. z=5 n=3 m= z-n
# y = (( (z+2-n)^2 * m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3

z = 5
n = 3
m = z-n
pasouno = (z+2-n)**2
pasodos = pasouno * 2 + 8 / 2 - 30
pasotres = (pasodos / 2 * 5 - 3) **5
pasocuatro = 15 * 3 - 9/3
final = pasotres + pasocuatro
print("Primer paso: (z+2-n)**2 = ",pasouno)
print("Segundo paso: (( (z+2-n)^2 * m+8/2 -30 ) / 2 * 5 -3)^ 5 = ",pasodos)
print("Tercer paso: 15 * 3 - 9/3 = ", pasotres)
print("Resultado final = ", final)
print("")

# 3. z=5 n=( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3 m= z^2*3+n
# y = ((( (z+2-n)^2 x m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 - 5/4

print("Calcular y = ((( (z+2-n)^2 x m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4" + "\n" + 
      "z=5  n=( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3  m= z^2*3+n")
z=5
n=((8+2-4)**2 * 5+8+7/2 -30*5 ) / 2 * 5 -3
m= z**2*3+n
pasouno = (z+2-n)**2
pasodos = pasouno * 2 + 8 / 2 - 30
pasotres = (pasodos / 2 * 5 - 3) **5
pasocuatro = 15 * 3 - 9/3
final = (pasotres + pasocuatro)**2 - 5/4
print("Resultado final = ", final)
print("")

# Realizar los algoritmos que den solución a la problemática presentada en los siguientes ejercicios:

# 1. Haga un algoritmo que calcule la masa de la siguiente fórmula: Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
print("1/ Calcule la masa con su formula:  Masa = (presion * volumen) / (0.37 * (temperatura + 460)) ")
volumen = int(input("Escriba el valor del volumen: "))
presion = int(input("Escriba el valor de la presion: "))
temperatura = int(input("Escriba el valor de la temperatura: "))
masa =  (presion * volumen) / (0.37 * (temperatura + 460))
print("El valor de la masa es: ", masa)
print("")

# 2. Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la fórmula es: Num. Pulsaciones = (200 – edad) /10.
print("2/ Calcule las pulsaciones con su formula: Num. Pulsaciones = (200 - edad) /10.")
edad = int(input("Digite su edad: "))
pulsaciones = int((200 - edad) / 10)
print("El numero de pulsaciones que usted tiene es: ", pulsaciones)
print("")

# 3. Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentajeque cada quien invierte con respecto a la cantidad total invertida.
print("3/ Porcentaje de la inversion con respecto a la total")
inversion1 = int(input("Inversion de la primera persona: "))
inversion2 = int(input("Inversion de la segunda persona: "))
inversion3 = int(input("Inversion de la tercera persona: "))

inversionTotal = inversion1 + inversion2 + inversion3

porcentaje1 = (inversion1/inversionTotal) * 100
porcentaje2 = (inversion2/inversionTotal) * 100
porcentaje3 = (inversion3/inversionTotal) * 100

print("Porcentaje de la primera persona: ",porcentaje1, "%")
print("Porcentaje de la segunda persona: ",porcentaje2, "%")
print("Porcentaje de la tercera persona: ",porcentaje3, "%")
print("")

# 4. Un banco da a sus ahorradores un interes de 1.5% sobre el monto ahorrado. Teniendo como dato de entrada el saldo inicial del ahorrador determine el saldo final.

print("4/ Determinar saldo final del ahorrador")
montoAhorrado = int(input("Monto ahorrado de la persona: "))
saldoInteres = (0.015 * montoAhorrado)
total = saldoInteres + montoAhorrado
print("El saldo final es: ", total)
print("")

# 5. Una empresa le hace los siguientes descuentos sobre el sueldo base a sus trabajadores: 1% por ley de politica pública, 4% por seguro social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un algoritmo que determine el monto de cada descuento y el monto total a pagar al trabajador.
print("5/ Determinar el descuento que se hace al sueldo individualmente y el total")
sueldo = int(input("Digite el sueldo sin descuentos: "))
leyPolitica = int((sueldo * 0.01))
seguroSocial = int((sueldo * 0.04))
seguroForzoso = int((sueldo * 0.005))
cajaAhorro = int((sueldo * 0.05))
montoTotal = int((sueldo - leyPolitica - seguroSocial - seguroForzoso - cajaAhorro))
print("Monto total a pagar: ",montoTotal)
print("")

# 6. El periódico el Informador cobra por un aviso clasificado un monto que depende del número de palabras, tamaño en cetímetros y número de colores. Cada palabra tiene un costo de $20.000, cada centímetro tiene un costo de $15.000 y cada color tiene un costo de $25.000. Realice un algoritmo que determine el monto a pagar por un aviso clasificado.
print("6/ Determine el monto a pagar por un aviso clasificado.")
palabras = 20000
centimetro = 15000
colores = 25000
valorP = int(input("Numero de palabras que llevara el periodico: "))
valorCen = int(input("Centimetros que llevara el periodico: "))
valorCo = int(input("Numero de colores que llevara el periodico: "))
total = ((palabras * valorP) + (centimetro * valorCen) + (colores * valorCo))
print("El monto a pagar por el aviso clasificado es: ", total)
print("")

# 7. Una empresa paga a sus empleados un bono por antigüedad que consiste en $100.000 por el primer año laboral y $120.000 por cada año siguiente. Realice un algoritmo que determine el monto del bono a pagar a un trabajador que tiene varios años en la empresa.
print("7/ Determine el valor del bono del trabajador")
bono1 = 100000
bono2 = 120000
años = int(input("Cuantos años lleva el trabajador? "))
if años < 1:
    print("No lleva el año")
elif años==1: 
    print("El bono del trabajador es: ",bono1)
else:
    total = bono1 + (bono2* (años-1))
    print("El bono del trabajador es: ", total)
print("")

# 8. Una Universidad le paga a sus profesores $20.000 la hora y le hace un descuento del 5% por concepto de caja de ahorro. Determine el monto del descuento y el monto total a pagar al profesor.
print("8/ Determinar el monto total a pagar al profesor")
pagoHora = 20000
descuento = 0.05
horas = int(input("Horas que trabajó el profesor: "))
montoDescuento = pagoHora * descuento
total = (pagoHora - montoDescuento) * horas
print("El monto total a pagar al profesor es: ",total)
print("")

# 9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas y cobran el monto consumido de la tarjeta mas un recargo del 20%. Teniendo como dato de entrada el monto inicial y el monto final de la tarjeta, determine el costo de la llamada.
print("9/ Determinar el costo de la llamada")
inicial = int(input("Monto inicial de la tarjeta: "))
final = int(input("Monto final de la tarjeta: "))
recargo = (inicial - final ) * 0.2
total = (inicial - final) + recargo
print("El costo de la llamada es: ",total)
print("")

# 10. En una fototienda cobran por el revelado de un rollo $1.500 por cada foto. Realice un algoritmo que determine el monto a pagar por un revelado completo sabiendo que adiconalmente le cobran el IVA (16%).
print("10/ Determinar monton a pagar con el iva")
rollo = 1500
revelados = int(input("Cuantos revelados se haran? "))
cobradoIva = (rollo * revelados) * 0.16
total = (rollo * revelados) + cobradoIva
print("El monto a pagar por los revelados con el iva es: ",total)
print("")

# 11. En un hospital existen tres áreas: Ginecología, Pediatría y Traumatología. El presupuesto anual del hospital se reparte conforme a la siguiente tabla:
# - Ginecologia 40%
# - Traumatologia 30%
# - Pediatria 30%
#Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal.
print("11/ Determinar presupuesto por area")
presupuesto = int(input(" Presupuesto total para el hospital: "))
ginecologia = presupuesto * 0.40
traumatologia = presupuesto * 0.30
pediatria = presupuesto * 0.30
print(" El presupuesto para ginecologia es: ",ginecologia, "\n",
      "El presupuesto para traumatologia es: ", traumatologia, "\n",
      "El presupuesto para pediatria es: ",pediatria)
print("")

# 12. Una video tienda alquila DVD a $1.500 el día. Tiene una promoción que consiste en dejar gratis el alquiler de una película. Realice un algoritmo que teniendo como dato de entrada el total de películas alquiladas, y el número de días de alquiler, determine el monto a pagar.
print("12/ Determinar monto a pagar por las peliculas alquiladas")
dvd = 1500
dias = int(input("Numero de dias alquilados: "))
peliculas = int(input("Numero de peliculas alquiladas: "))
total = (dias * dvd ) * (peliculas - 1)
print("El total a pagar es: ",total)
print("")

# 13. Una Agencia de viajes cobra por un Tour a Cartagena $25.000 diarios por persona. Realice un algoritmo que determine el monto a pagar por una familia que desee realizar dicho Tour sabiendo que también cobran el 12% de IVA.
print("13/ Determinar el monto a pagar de una familia en el tour")
tour = 25000
dias = int(input("Numero de dias en el tour: "))
personas = int(input("Numero de personas en el tour: "))
iva = (tour * dias * personas) * 0.12
total = (tour * dias * personas) + iva
print("El monto a pagar de la familia es: ",total)
print("")

# 14. Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus clientes. Cobra por una habitación $100.000 el primer día y por el resto $200.000 por día. 
# Realice un algoritmo que determine el valor total a pagar por la habitación si la estadía fue de varios días.
print("14/ Determine el monto a pagar por la habitacion")
primerDia = 100000
resto = 200000
dias = int(input("Numero de dias de estadia en la habitacion: "))
if dias <= 1:
    print("El valor a pagar es: $",primerDia)
else:
    total = primerDia + (resto * (dias -1))
    print("El valor a pagar es: $",total)
print("")

# 15. El banco del Pueblo da microcréditos a empresarios para ser cancelados en un lapso de 2 años (24 meses). Al monto del préstamo se le cobra un interés del 24%.
# El empresario debe pagar la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20 cuotas ordinarias. Realice un algoritmo que teniendo como dato de entrada el monto del préstamo, determine el monto total a pagar por el préstamo, el monto de las cuotas especiales y el monto de las cuotas ordinarias.
print("15/ Determinar el monto total a pagar por el prestamo")
prestamo = int(input("Ingrese monto del prestamo: "))
periodo = 24
interes = prestamo * 0.24
total = prestamo + interes
separacionCuotas = total / 2
especiales = (separacionCuotas / 4)
ordinarias = (separacionCuotas / 20)
print("El monto total a pagar es: ",total)
print("El monto a pagar en cuotas especiales es: ",especiales)
print("El monto a pagar en cuotas ordinarias es: ",ordinarias)
print("")
