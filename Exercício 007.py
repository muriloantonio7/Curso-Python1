'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
n1 = float(input('A nota da avaliação 01: ')) #Float por ser nota, e isso não necessariamente será valor inteiro
n2 = float(input('A nota da avaliação 02: '))
# m = n1 + n2 / 2 #ERRADO OBSERVAR PRECEDÊNCIA!!!!!!!!!!!!!!!!!!!!!!!
m = (n1+n2)/2
print('considerando as notas {} e {} a média restou {}'.format(n1,n2,m))
#Se quiser que após a vírgula, no resultado, apareça somente duas casas (exemplo)
#após, digita-se {:.2f} dentro das {} que deseja que apareça as duas casas