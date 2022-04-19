'''
Uma estrutura condicional, como o próprio nome já diz é uma estrutura que vai analisar uma condição
e baseado no resultado dessa condição é que vamos executar uma determinada ação.

IF - "se"
ELSE - "senão"
ELIF - "
'''


#tempo = int(input('Quantos anos seu carro possui? '))
#if tempo <= 3:
#    print('Seu carro é novo!')
#else:
#    print('Seu carro é velho ):')
# SIMPLIFICADO
# print('carro novo'if tempo <=3 else'carro velho')


#nome = str(input('Qual é o seu nome? '))
#if nome == 'Murilo'.upper().lower():
#    print('WHAT A BEAUTIFUL NAME!!!')
#else:
#    print('Que nome bosta kkkkk')
#print('Bom dia {}!'.format(nome))


n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2) / 2
print('A sua média foi {}'.format(media))
if media >=6:
    print('PARABÉNS, APROVADO!')
else:
    print('TENTE NOVAMENTE, REPROVADO ):')


