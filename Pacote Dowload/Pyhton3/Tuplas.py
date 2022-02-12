# Tuplas são IMUTÁVEIS
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2])
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi para caramba!')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi para caramba!')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi para caramba!')
print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(5, 1))
pessoa = ('Gustavo', 39, 'M', 99.88)
del pessoa

