'''
============PARTE I=============
Laço = for
no = in
intervalo = range
'''

# for c in range (0,10):
#    print('oi') # PRINT AO LADO DIREITO POIS ESTÁ DENTRO DO FOR E COM ISSO SE REPETIRÁ
# print('FIM')


# SE QUISER CONTAR PRA TRAS

# for c in range (6,0,-1):
#    print(c)
# print('FIM')


# SE QUISER PULAR DE 2 EM 2

# for c in range (0,10,2):
#    print(c)


# SE QUISER FAZER COM QUE O USUARIO DIGITE O NUMERO

# n = int(input('Digite um número: '))
# for c in range (0, n+1): # n é a variável que defini e, +1, para que o programa seja lido de acordo com o que o usuario deseja.
#    print(c)
# print('Fim')


# PULANDO DE DOIS EM DOIS DANDO NOME PARA AS VARIAVEIS

# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range (i, f+1, p): # Inicia a contagem do i até o f, considerando quantos passos o usuario deseja avançar
#    print(c)
# print('FIM')


# SOMANDO VALORES QUE APARECEREM REPETIDAMENTE

s = 0
for c in range (0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório dos números digitados foi de {}'.format(s))















