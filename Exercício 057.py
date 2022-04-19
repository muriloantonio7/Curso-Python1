'''

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.

Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Digite o seu sexo: [M/F] ')).upper()[0].strip()
m = 'masculino'
f = 'feminino'
while sexo not in 'MmFf':
    sexo = str(input('Código inválido. Por favor, digite novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

