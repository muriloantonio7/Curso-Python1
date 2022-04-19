'''

Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.

Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

'''
from random import randint
computador = randint(0,10)
print('Olá!')
print('Vou pensar em um número entre 0 e 10... tente adivinhar')
print('-=-'*20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
print('PARABÉNS, você me venceu com {} palpites!.'.format(palpite))

