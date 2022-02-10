from random import randint
numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
menor = numbers[0]
maior = numbers[0]
for n in numbers:
    print(f'{n} ', end='')
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
print(f'\nO maior número sorteado foi {maior}.')
print(f'O menor número sorteado foi {menor}.')