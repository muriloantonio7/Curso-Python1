'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
salario = float(input('Qual o salário do funcionário X? R$'))
novo = salario + (salario * 15/100)

print('Funcionário X ganhava um salário de R${:.2f} mas com um aumento de 15% passou a receber R${:.2f}'.format(salario, novo))