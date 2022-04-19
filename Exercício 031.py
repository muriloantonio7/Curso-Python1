'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a iniciar uma viagem de {}km'.format(distancia))
if distancia <=200:
    valor1 = distancia*0.50
    print('O valor a cada km foi de R$0.50, portanto, para sua viagem o valor foi de R${:.2f}'.format(valor1))
else:
    valor2 = distancia*0.45
    print('O valor a cada km é de R$0.45, portanto, para sua viagem o valor foi de R${:.2f}'.format(valor2))