print('='*44)
print('                  BANCO CEV')
print('='*44)
valor = int(input('Qual valor você deseja sacar? '))
cinquenta = vinte = dez = cinco = dois = um = 0
while True:
    cinquenta = valor//50
    valor = valor - (cinquenta*50)
    vinte = valor//20
    valor = valor - (vinte*20)
    dez = valor//10
    valor = valor - (dez*10)
    cinco = valor//5
    valor = valor - (cinco*5)
    um = valor
    valor = valor - um
    if valor == 0:
        break
if cinquenta > 0:
    print(f'Total de {cinquenta} cédulas de 50 reais')
if vinte > 0:
    print(f'Total de {vinte} cédulas de 20 reais')
if dez > 0:
    print(f'Total de {dez} cédulas de 10 reais')
if cinco > 0:
    print(f'Total de {cinco} cédulas de 5 reais')
if um > 0:
    print(f'Total de {um} moedas de 1 real')
print('=' * 44)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
print('=' * 44)