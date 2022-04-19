'''

Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,

mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''

print('='*10, 'GERADOR DE PA', '='*10)
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = pt
c = 1
while c <= 10:
    print('{} -> '.format(termo),end=' ')
    termo += razao
    c += 1
print('FIM')
