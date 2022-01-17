sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo == 'F':
    print('Sexo FEMININO registrado com sucesso!')
elif sexo == 'M':
    print('Sexo MASCULINO registrado com sucesso!')
