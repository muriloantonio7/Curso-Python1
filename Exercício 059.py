'''

Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

'''

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''Escolha uma das opções abaixo para ser realizada:'
[ 1 ] Somar 
[ 2 ] Multiplicar
[ 3 ] Maior 
[ 4 ] Novos números
[ 5 ] Sair do Programa''')
    opção = int(input('Digite sua opção: '))
    if opção == 1:
        soma = valor1+valor2
        print('A soma entre {} e {} resultará em {}'.format(valor1,valor2,soma))
    elif opção == 2:
        multiplica = valor1*valor2
        print('A multiplicação entre {} e {} resultará no produto {}'.format(valor1, valor2, multiplica))
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
    elif opção == 4:
        print('Informe os números novamente!')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.')


print('Fim do programa.')





