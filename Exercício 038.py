'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num2,num1))
else:
    print('Não existe valor maior, os dois são iguais!')
