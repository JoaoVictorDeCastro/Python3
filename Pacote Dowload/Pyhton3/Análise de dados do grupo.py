dezoito = homens = mulheres = 0
sexo = continuar = ' '
while True:
    print('-'*23)
    print('  CADASTRE UMA PESSOA  ')
    print('-' * 23)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        dezoito += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade <= 20:
            mulheres += 1
    print('-' * 23)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    continuar = sexo = ' '
print('-' * 23)
print(f'O total de pessoas com mais de 18 anos é {dezoito}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'Temos {mulheres} mulheres com menos de 20 anos cadastradas. ')