'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
num = int(input('Digite um número: '))
print('Analisando o número {}...........'.format(num))
#print('A sua unidade é {}'.format(n[3]))
#print('A dezena é {}'.format(n[2]))
#print('A centena é {}'.format(n[1]))
#print('E o milhar é {}'.format(n[0]))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade é {}'.format(u))
print('Dezena é {}'.format(d))
print('Centena é {}'.format(c))
print('Milhar é {}'.format(m))

