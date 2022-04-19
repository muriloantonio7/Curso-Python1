'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = real / 5.03
print('Com o valor de R${}, você pode comprar US${:.2f}'.format(real,dol))