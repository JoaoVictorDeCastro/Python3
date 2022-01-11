primo = 's'
num = int(input('Digite um número:'))
for c in range(2, num):
    if num % c == 0:
        primo = 'n'
if primo == 'n':
    print('{} não é um número primo!' .format(num))
else:
    print('{} é primo!' .format(num))