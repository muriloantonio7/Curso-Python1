'''

Crie um programa que faça o computador jogar Jokenpô com você.

'''
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('O computador escolheu {}'.format(itens[computador]))
