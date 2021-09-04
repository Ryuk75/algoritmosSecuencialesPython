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
