'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''
nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Muito prazer em conhecê-lo, {}'.format(nome))
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))

