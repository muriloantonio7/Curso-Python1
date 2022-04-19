'''

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.

No final, mostre os 10 primeiros termos dessa progressão.

'''

print('='*10, '10 TERMOS DE UMA PA', '='*10)
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(pt, 11, razao):
    print('{}'.format(c))
print('ACABOU')
