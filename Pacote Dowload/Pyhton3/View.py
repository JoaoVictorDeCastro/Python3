num = 1
while num == 1:
    nome = input('Qual o seu nome? ')
    idade = int(input('Qual a sua idade? '))
    sexo = input('Qual o seu gênero? [M,F] ').strip().upper()
    print('----- Informações -----')
    print('Nome: {}.' .format(nome))
    print('Idade: {}.' .format(idade))
    if sexo == 'M':
        print('Gênero: Masculino.')
    elif sexo == 'F':
        print('Gênero: Feminino.')
    else:
        print('Gênero: Prefere não informar.')