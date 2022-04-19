'''
Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender:
Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(),
capitalize(), title(), strip(), junção com join().
'''
# Fatiamento
# >>> s = 'Monty Python'
# >>> s[0:5]
# 'Monty'
# >>> s[6:12]
# 'Python'
# Conforme exemplo acima, vemos que a frase 'monty python' está descrita como 0 = M , 1 = o , 2 = n ...
# Sendo assim, na linha 8, foi selecionado 0:5 portanto, da caixa 0 até a 5, ou seja, buscou a palavra MONTY
# Já na linha 10, foi solicitado do 6:12 o que gero5]u o print PYTHON

# AINDA,
# caso seja indicado [0:5:2], por exemplo, será feito da caixa 0 até a 5, porém pulando de duas em duas cxs

# Quando está [:5], não estando determinada aonde inicia a contagem, iniciará na caixa 0
# já quando ocorre o oposto [5:] ele iniciará na caixa 5 e não terá limite definido, indo até o final do programa
# Se for [0::3], ele iniciará no 0, não terá final estabelecido e, pulará de 3 em 3 casas

# ----------FUNÇÕES----------

# ----------len = comprimento da frase
frase = 'Curso em vídeo python'
print(len(frase))
# ----------count = 'curso em video' frase.count('o') a função contará quantas vezes aparece a letra 'o' na tela
print(frase.count('o')) # caso específico 'frase1.count('o',0,5) verá quantos 'o' tem entre 0 e 5
# ----------find = frase.find('deo') ele localizará o número da caixa em que começa a expressão 'deo'
print(frase.find('deo')) # se caso pedir por algo que não existe, retornará o valor -1
# ----------transformação = frase.replace('Python', 'Android')
# seria trocado a palavra python por android
print(frase.replace('python','android'))
# ----------upper = analisará as letras maiusculas usa-se com () pois é um método
# oq já estava maiusculo na frase permanece, e o que estava minusculo passa a ser maiusculo
print(frase.upper())
# ----------lower = o oposto de upper, letras minusculas
print(frase.lower())
# ----------capitalize = pega uma string inteira, joga tudo pra minusculo, MENOS a primeira letra da str
print(frase.capitalize())
# ----------title = analisa quantas palavras tem na string
print(frase.title()) # todo inicio de palavra é feito com a primeira letra maiuscula
# ----------strip = removerá todos os espaços inuteis no inicio e final das palavras
frasestrp = '          curso em vídeo        '
print(frasestrp.strip())
print(frasestrp.rstrip())
print(frasestrp.lstrip())
# -----------split = desmembra a string 
print(frase.split())