'''

Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.

O programa encerrará quando ele disser que quer mostrar 0 termos.

'''
print('='*10, 'GERADOR DE PA', '='*10)
pt = int(input('Digite o primeiro de uma PA: '))
razao = int(input('Digite a razão: '))
termo = pt
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        c += 1
print('PAUSA')
mais = int(input('Deseja mostrar mais quantos termos? '))

