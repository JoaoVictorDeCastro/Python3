n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
n3 = int(input('Digite um terceiro valor:'))
if n1 > n2 and n1 > n3:
    print('O maior valor foi {}' .format(n1))
    if n2 > n3:
        print('O menor valor foi {}'.format(n3))
    else:
        print('O menor valor foi {}' .format(n2))
elif n2 > n1 and n2 > n3:
    print('O maior valor foi {}' .format(n2))
    if n1 > n3:
        print('O menor valor foi o {}' .format(n3))
    else:
        print('O menor valor foi o {}' .format(n1))
else:
    print('O maior valor foi {}' .format(n3))
    if n1 > n2:
        print('O menor valor foi {}' .format(n2))
    else:
        print('O menor valor foi {}' .format(n1))