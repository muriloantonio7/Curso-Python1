'''
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1,n2,n3,n4] # em SHUFFLE utilizar ------COLCHETES------
random.shuffle(lista) # SHUFFLE serve para EMBARALHAR a lista
print('A ordem do sorteio ficou {}:'.format(lista))
