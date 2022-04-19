nome = str(input('Digite seu nome: '))
if nome == 'Murilo':
    print('Você tem um nome muito bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Você tem um nome muito comum no Brasil.')
elif nome in 'Marcia Creusa Paulo Marco':
    print('Nome naskiera!!!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))
