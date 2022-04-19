'''
Um módulo é um arquivo contendo definições e comandos em Python para serem usados em outros programas em Python.

Exemplo: Biblioteca MATH

utiliza-se #import para trazer as bibliotecas para o programa caso queira trazer toda biblioteca a tona
caso queira algo específico, usa-se (from math import ceil/floor/trunc/pow/sqrt/factorial)
ceil = arredonda pra cima
floor = pra baixo
trunc = eliminar da virgula pra frente sem fazer arredondamento
pow = potencia
sqrt = raiz quadrada (square root)
'''
# CALCULE A RAIZ QUADRADA DE UM NUMERO ------ PRÁTICA
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))
