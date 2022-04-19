'''

Escreva um programa que leia um número N inteiro qualquer

e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

Exemplo:

sempre inicia com 0 e 1

0 – 1 – 1 – 2 – 3 – 5 – 8

após, 1 + 0 = 1
1 + 1 = 2
2 + 1 = 3
3 + 2 = 5
5 + 3 = 8
'''
print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0 #Sempre o primeiro termo vai ser 0
t2 = 1 #E o segundo será 1
print('-'*30)
print('{} -> {}'.format(t1,t2), end=' ')
cont = 3 # pois já foi mostrato o t1 e o t2
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end=' ')
    t1 = t2
    t2 =t3
    cont += 1
print('FIM')