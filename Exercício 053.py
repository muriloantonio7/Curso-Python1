'''

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,

desconsiderando os espaços.

------- Exemplos de palíndromos:

-> APOS A SOPA,
-> A SACADA DA CASA,
-> A TORRE DA DERROTA,
-> O LOBO AMA O BOLO,
-> ANOTARAM A DATA DA MARATONA.

'''
frase = str(input('Digite uma frase: ')).strip().upper() # strip é para tirar os espaços
palavras = frase.split() #dividir as palavras da frase
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1): #len é para contar o número de letras da frase'''
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('PALÍNDROMO')
else:
    print('A frase digitada NÃO é um palíndromo')
