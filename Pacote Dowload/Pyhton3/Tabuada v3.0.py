cont = 1
print('-' * 34)
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 34)
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {cont} = {tabuada*cont}')
        cont += 1
    print('-' * 34)
print('Programa de tabuada ENCERRADO! Volte Sempre!')