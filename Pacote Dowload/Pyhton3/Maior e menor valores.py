resposta = 's'
menor = maior = total = cont = 0
while resposta != 'N':
    n = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    cont += 1
    total = n + total
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = total/cont
print('Você digitou {} números e a média entre eles foi {:.2f}' .format(cont, media))
print('O maior valor foi {} e o menor foi {}' .format(maior, menor))
