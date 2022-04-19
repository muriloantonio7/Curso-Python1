'''

Crie um programa que leia vários números inteiros pelo teclado.

No final da execução, mostre a média entre todos os valores

e qual foi o maior e o menor valores lidos.

O programa deve perguntar ao usuário se ele quer ou não

continuar a digitar valores.

'''
resp = 'S'
media = 0
soma = 0
quantidade = 0
maior = 0
menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média entre eles foi {}'.format(quantidade,media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))