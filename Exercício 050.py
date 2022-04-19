'''

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.

Se o valor digitado for ímpar, desconsidere-o.

'''
#s = 0
#n1 = int(input('Primeiro número: '))
#n2 = int(input('Segundo número: '))
#n3 = int(input('terceiro número: '))
#n4 = int(input('Quarto número: '))
#n5 = int(input('Quinto número: '))
#n6 = int(input('Sexto número: '))
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += + 1
print('Você informou {} números PARES e a soma deles é {}'.format(cont, soma))
