'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura**2)
print('Seu IMC é {:.2f}'.format(IMC))
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC < 25:
    print('PESO IDEAL')
elif IMC < 30:
    print('SOBREPESO')
elif IMC < 40:
    print('OBESIDADE')
elif IMC > 40:
    print('OBESIDADE MÓRBIDA')