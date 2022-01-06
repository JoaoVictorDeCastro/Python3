#Primeiro exercício
idade = int(input('Qual a sua idade?'))
if idade < 18:
    print('Você ainda deverá  aguardar um pouco para dirigir.')
else:
    print('Parabéns, você já pode tirar sua habilitação!')
#Segundo exercício
n1 = int(input('Digite um número:'))
n2 = int(input('Digite o segundo número:'))
if n1 > n2:
    print('O maior número é {}.' .format(n1))
elif n1 == n2:
    print('Os dois números são iguais e valem {}' .format(n1))
else:
    print('O maior número é {}.'.format(n2))
