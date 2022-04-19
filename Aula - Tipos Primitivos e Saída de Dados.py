# n1 = input('Digite um número: ')
# n2 = input('Digite mais um número: ')
# s = n1+n2
# print('A soma vale: {}'.format(s))
# print('A soma vale: ', s) # não ocorre a soma, mas sim a concatenação,
# DEVE-SE então colocar int(input('Digite um número: ')) p/ mostrar q o q quer que apareça na tela é um número


'''
EXEMPLO

n1 = input('Digite um valor: ')
print(type (n1)) # mostrará Class 'STR' ao invés de INT

já se colocarmos,

n1 = int(input('Digite um valor: '))
print(type(n1)) mostrará Class 'INT' como era preterido
'''


#n1 = int(input('Digite um número: '))
#n2 = int(input('Digite outro número: '))
#s = n1+n2
#print('A soma vale: {}'.format(s))

# PROFESSOR SOLICITOU QUE APAREÇA ' A SOMA DO N1 + A SOMA DO N2 É IGUAL Á...

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
# print('A soma entre', n1, 'e', n2, 'é igual a ', s)
print('a soma entre {} e {} vale {}'.format(n1, n2, s))