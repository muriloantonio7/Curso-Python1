'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.

Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o salário do comprador? '))
periodo = int(input('Em quanto tempo deseja pagar? '))
prestação = casa / (periodo * 12)
minimo = salario * 30 / 100 ######## 30 porcento do salário
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,periodo))
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('EMPRESTIMO CONCEDIDO')
else:
    print('EMPRESTIMO NEGADO!')