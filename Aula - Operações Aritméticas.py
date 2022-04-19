"""

OPERADORES ARITMETICOS
+ , - , * , / , // , ** , % , ()

+ = ADIÇÃO / CONCATENAÇÃO
- = SUBTRAÇÃO
* = MULTIPLICAÇÃO // também serve como repetição
/ = DIVISÃO
// = DIVISÃO INTEIRA (RESULTADO ARREDONDADO)
** = POTENCIAÇÃO (10³)
% = RETORNA O MÓDULO (RESTO DA DIVISÃO ENTRE UM NUMERO E OUTRO)
"""
# print('adição 10+10 =', 10+10)
# print('subtração 15-5 =', 15-5)
# print('multiplicação 25*2 =', 25*2)
# print('divisão 30/2 =', 30/2)
# print('divisão inteira 25//3 =',25//3)
# print('multiplicação / repetição =',10*'10')
# print('concatenação =','5'+'5')
# print('retorno da divisão =', 10%2)
# print('retorno 2 =',10%3)

# ORDEM DE PRECEDÊNCIA

# 1 : ()
# 2 : **
# 3 : * , /, // , %
# 4 : + , -

# EXEMPLO

# 5+3*2 = primeiro ordem 3 (3x2=6) depois ordem 4 (5+ resultado de 3x2)
# 3*5+4**2 = primeiro ordem 2 (4**2=16) depois ordem 3 (3*5=15) após isso,
# ordem 4 (soma entre 16+15=31)

# PARA CALCULAR RAIZ
# 25**(1/2) raiz quadrada
# 127**(1/3) raiz cúbica

n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
ex = n1 ** n2

print('A soma é {}\n o produto é {}\n e a divisão é {}'.format(s, m, d)) # \n
print('divisão inteira é {}, a potencia é {}'.format(di, ex))
