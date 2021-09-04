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

