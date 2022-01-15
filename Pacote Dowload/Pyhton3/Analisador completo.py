idade_total = 0
maior_idade = 0
mulher_menor20 = 0
homem_idade = 0
for ac in range(1, 5):
    print('----- {}º PESSOA -----' .format(ac))
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idade_total = idade_total + idade
    if idade > maior_idade:
        maior_idade = idade
        nome_maior_idade = nome
    if sexo == 'M':
        if idade > homem_idade:
            homem_idade= idade
            nome_homem = nome
    if idade < 20 and sexo == 'F':
        mulher_menor20 += 1
média = idade_total/4
print('A média de idade do grupo é de {}.' .format(média))
print('O homem mais velho tem {} anos e se chama {}.' .format(homem_idade, nome_homem))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(mulher_menor20))