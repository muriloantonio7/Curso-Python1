'''

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

'''
num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m',end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c,end= ' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('Por isso, NÃO é primo')

