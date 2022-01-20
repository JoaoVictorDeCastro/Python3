cont = c = soma = 0
while c != 999:
    c = int(input('Digite um número [Digite 999 para PARAR]: '))
    if c != 999:
        cont += 1
        soma += c
print('Você digitou {} números e a soma entre eles foi {}.' .format(cont, soma))
