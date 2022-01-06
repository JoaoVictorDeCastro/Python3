salario = float(input('Qual o seu salário atual? R$'))
if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + ( salario * 15 / 100)
print('Com aumento, seu salário será de R${:.2f}' .format(aumento))
