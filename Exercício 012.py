'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
original = float(input('Qual o preço do produto? R$'))
desconto = original - (original * 5 / 100) #se colocado ori*5/100 não mostrará o novo valor e sim o desconto
print('O valor original do produto é R${} porém com desconto ficará R${:.2f}'.format(original,desconto))