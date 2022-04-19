'''

Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

'''
# n = int(input('Digite um número: '))
# n1 = n*1
# n2 = n*2
# n3 = n*3
# n4 = n*4
# n5 = n*5
# n6 = n*6
# n7 = n*7
# n8 = n*8
# n9 = n*9
# n10 = n*10
# print('-'*20)
# print('A tabuada de {} é{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(n,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))
# print('-'*20)
num = int(input('Digite um número para a sua tabuada: '))
for c in range (0,11):
    print('{} x {} = {}'.format(num, c, num*c))