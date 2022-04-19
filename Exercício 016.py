'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

Exemplo: Digite um número: 6127
O número 6127 tem a parte inteira 6.

utilizar 'math.trunc'
'''

#from math import trunc
#num = float(input('Digite um número: '))
#print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

# AINDA, esse exercício pode ser resolvido colocando 'int' ao invés de trunc (linha 12)

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))
