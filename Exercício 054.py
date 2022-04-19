'''

Crie um programa que leia o ano de nascimento de sete pessoas.

No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''
from datetime import date
totmaior = 0
totmenor = 0
for c in range(1,8):
    nasc = int(input('Digite o {}° ano de nascimento: '.format(c)))
    atual = date.today().year
    idade = atual - nasc
    print('a pessoa tem {} anos'.format(idade))
    if idade >= 18:
        totmaior = totmaior+1
    else:
        totmenor = totmenor+1
print('Ao todo {} pessoas são maiores de idade e {} são menores'.format(totmaior, totmenor))



