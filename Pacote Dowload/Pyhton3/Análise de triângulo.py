print('-=-'*10)
print('   Analisador de triângulos')
print('-=-'*10)
l1 = float(input('Qual o tamanho do primeiro lado:'))
l2 = float(input('Qual o tamanho do segundo lado:'))
l3 = float(input('Qual o tamanho do terceiro lado:'))
if l1 > l2 + l3 and l2 > l1 + l3 and l3 > l1 + l2:
    print('Esses segmentos podem formar um triângulo')
else:
    print('Esses segmentos NÃO podem formar um triângulo')
