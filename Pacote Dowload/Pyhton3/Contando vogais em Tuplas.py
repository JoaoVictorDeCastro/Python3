palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for pl in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[pl]} temos: ', end='')
    if 'A' in palavras[pl]:
        print('A', end=' ')
    if 'E' in palavras[pl]:
        print('E', end=' ')
    if 'I' in palavras[pl]:
        print('I', end=' ')
    if 'O' in palavras[pl]:
        print('O', end=' ')
    if 'U' in palavras[pl]:
        print('U', end=' ')