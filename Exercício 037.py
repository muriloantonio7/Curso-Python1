'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário

escolher qual será a base de conversão:

1 para binário, 2 para octal e 3 para hexadecimal.
'''
numero = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:'
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(numero, bin(numero)[2:])) ### FATIEI A STR iniciando a partir da segunda casa
elif opção == 2:
    print('{} convertido em OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format((numero, hex(numero)[2:])))
else:
    print('Opção inválida. Tente novamente.')
