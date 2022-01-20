from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
end = False
resposta = 0
while not end:
    print('     [ 1 ] Somar')
    print('     [ 2 ] Multiplicar')
    print('     [ 3 ] Maior')
    print('     [ 4 ] Novos números')
    print('     [ 5 ] Sair do programa')
    resposta = int(input('>>>>> Qual a sua opção? '))
    if resposta == 1:
        print('A soma entre {} e {} é {}.' .format(n1, n2, n1+n2))
    elif resposta == 2:
        print('A multiplicação entre {} e {} é {}.' .format(n1, n2, n1*n2))
    elif resposta == 3:
        if n1 > n2:
            print('O maior número entre os digitados é {}.' .format(n1))
        elif n1 == n2:
            print('O dois números são iguais.')
        else:
            print('O maior número entre os digitados é {}' .format(n2))
    elif resposta == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        end = True
    print('-=='*10)
    sleep(1)
