'''

Nessa aula, vamos aprender como utilizar a instrução BREAK e os

loopings infinitos a favor das nossas estratégias de código.

É muito importante saber usar o break no Python, já que

em alguns casos precisamos interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

'''
'''n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma entre os valores vale: {}'.format(s))'''

# Se o programa acima fosse executado dessa forma,
# ao realizar o comando 's' de soma, somaria junto o '999'
# comando esse que não deveria fazer parte da soma e sim, gatilho para
# que o programa parasse.
# PORTANTO, utiliza-se o ---BREAK---

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}') # uso de --->FSTRINGS<---