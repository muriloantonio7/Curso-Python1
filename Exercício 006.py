'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
n = int(input('Digite um valor: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} vale {}.'.format(n,d))
print('O triplo de {} vale {} \n' 'A raiz quadrada de {} vale {}'.format(n,t,n,r))
