'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo)) # SEMPRE SE CONVERTE PARA RADIANOS
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O cosseno de {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(angulo))
print('E o tangente é {:.2f}'.format(tangente))
