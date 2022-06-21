
#15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
#salário de um funcionário, sabendo que ele trabalha 10 horas por dia e ganha R$25
#por hora trabalhada.

dias = float(input('Informe a quantidade de dias trabalhados no mês: '))

salario = (25*10)*dias

print('Ao final do mês, o funcionário deverá receber: ' + str(salario))