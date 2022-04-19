'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
v = float(input('Uma distância em metros: '))
centimetros = v * 100
m = v * 1000
print('A medida de {}m corresponde, em centímetros a {}cm e em milímetros a {}mm'.format(v,centimetros,m))