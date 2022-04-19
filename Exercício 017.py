'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''

#FÓRMULA TEOREMA DE PITÁGORAS = a² = b² + c²
# a = hipotenusa
# b = cateto adjacente
# c = cateto oposto

#from math import ceil
import math
b = float(input('Comprimento do cateto adjacente: '))
c = float(input('Comprimento do cateto oposto: '))
# a = (b ** 2 + c ** 2) ** (1/2) sem o 'math.hypot'
a = math.hypot(b,c)
print('O comprimento da hipotenusa é {:.2f}'.format(a))




