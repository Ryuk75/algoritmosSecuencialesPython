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