while True:
    cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
            'dezoito', 'dezenove', 'vinte')
    while True:
        num = int(input('Digite um número de entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {cont[num]}.')
    while True:
        resposta = str(input('Você deseja continuar? [s/n] ')).strip().upper()
        if resposta == 'S' or resposta == 'N':
            break
    if resposta == 'N':
        break
