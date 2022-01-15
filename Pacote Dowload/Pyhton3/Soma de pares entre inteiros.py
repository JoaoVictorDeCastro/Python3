cont = 0
for num in range (1,7):
    c = int(input('Digite um número inteiro:'))
    if c%2 == 0:
        cont = cont+c
print('A soma dos valores pares dos números digitados é {}' .format(cont))