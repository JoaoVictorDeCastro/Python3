print('-'*43)
print('            LOJA DO GUANABARA')
print('-'*43)
total = mil = 0
produto_menor = ' '
cont = 0
while True:
    cont += 1
    nome = input('Nome do produto: ')
    preço = float(input('Preço do produto: R$'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if cont == 1:
        menor = preço
    total += preço
    if preço >= 1000:
        mil += 1
    if preço < menor:
        produto_menor = nome
        menor = preço
    if continuar == 'N':
        break
print('------------- FIM DO PROGRAMA -------------')
print(f'O total da compra foi {total:.2f}')
print(f'Temos {mil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_menor} que custa R${menor:.2f}')
print('-'*43)
