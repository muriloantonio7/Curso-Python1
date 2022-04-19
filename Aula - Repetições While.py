'''

Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:

c=1 while c !=10:
print(c)
c+=1
print(‘Acabou’)

'''
'''For c in range(1,10):
    print(c)
print('FIM')'''

# IGUAL AO DE BAIXO

'''c = 1 # O contador começa com 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')'''

###########################################

'''for c in range(1,3):
    n = int(input('Digite um valor: '))
print('FIM')'''

# IGUAL AO DE BAIXO

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')'''

############################################
par = impar = 0
n= 1
while n != 0: #ENQUANTO n for diferente de 0, vai digitando valor...
    n = int(input('Digite um valor:'))
    if n != 0: # pra não considerar 0 par
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} ímpares.'.format(par, impar))
