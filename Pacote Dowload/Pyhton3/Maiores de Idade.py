from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    if date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print('Das sete pessoas digitadas {} são MAIORES DE IDADE.' .format(maior))
print('As outras {} pessoas são MENORES DE IDADE.' .format(menor))
