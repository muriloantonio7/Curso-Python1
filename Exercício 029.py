'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.
'''
velocidade = int(input('A velocidade medida foi: '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade permitido!')
    multa = (velocidade-80) * 7
    print('O valor da multa ficou em R${:.2f}'.format(multa))
else:
    print('Siga em frente!')
