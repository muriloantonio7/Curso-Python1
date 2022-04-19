'''

Elabore um programa que calcule o valor a ser pago por um produto,

considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros

'''
print('{:=^40}'.format('LOJAS GUANABARA'))
preço = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque 
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
elif opção == 4:
    totalparc = int(input('Quantas parcelas? '))
print('Sua compra de R${:.2f} ao final, custará R$ {:.2f} no final.'.format(preço, total))
