'''
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e,
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
computador = randint(0,5)
print('Olá!')
print('Vou pensar em um número entre 0 e 5... tente adivinhar')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('-=-'*20)
if jogador == computador:
    print('PARABÉNS, você me venceu!')
else:
    print('HAHAHAHAHA GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))


