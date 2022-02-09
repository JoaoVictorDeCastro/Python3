# Tuplas são IMUTÁVEIS
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2])
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi para caramba!')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi para caramba!')
