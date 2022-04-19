'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,

se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou

se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
# nascimento = int(input('Digite o ano de seu nascimento: '))
#idade = 2022 - nascimento
#if idade == 18:
#    print('Você deve se alistar neste ano!')
#elif idade > 18:
#    print('Você passou do tempo de alistamento! Procure uma Junta Militar!')
#elif idade < 18:
#    print('Você ainda não está em período de alistamento militar!')

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem anos {} em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos!'.format(saldo))
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Restam ainda {} ano(s) para isso.'.format(saldo))
