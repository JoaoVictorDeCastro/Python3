import math
#001
num = float(input("Digite um número:"))
print("A porção inteira do seu número é {}" .format(math.trunc(num)))
#002
CO = float(input("Digite o comprimento do cateto oposto:"))
CA = float(input("Digite o comprimento do cateto adjacente:"))
hipotenusa2 = math.pow(CO, 2) + math.pow(CA, 2)
hipotenusa = math.sqrt(hipotenusa2)
print("O valor da hipotenusa é {}".format(hipotenusa))
#003
import random
nome1 = input('Digite o nome do primeiro aluno:')
nome2 = input('Digite o nome do segundo aluno:')
nome3 = input('Digite o nome do terceiro aluno:')
nome4 = input('Digite o nome do quarto aluno:')
aluno = random.randint(1, 4)
if aluno == 1:
    print('O escolhido foi {}' .format(nome1))
else:
    if aluno == 2:
        print('O escolhido foi {}' .format(nome2))
    else:
        if aluno == 3:
            print('O escolhido foi {}'.format(nome3))
        else:
            print('O escolhido foi {}' .format(nome4))
#004
nome1 = input('Digite o nome do primeiro aluno:')
nome2 = input('Digite o nome do segundo aluno:')
nome3 = input('Digite o nome do terceiro aluno:')
nome4 = input('Digite o nome do quarto aluno:')
aluno1 = random.randint(1, 4)
if aluno1 == 1:
    print('O primeiro(a) a apresentar é {}' .format(nome1))
else:
    if aluno1 == 2:
        print('O primeiro(a) a apresentar é {}' .format(nome2))
    else:
        if aluno1 == 3:
            print('O primeiro(a) a apresentar é {}'.format(nome3))
        else:
            print('O primeiro(a) a apresentar é {}' .format(nome4))
aluno2 = random.randint(1, 4)
if aluno2 == aluno1:
    aluno2 = random.randint(1, 4)
if aluno2 == aluno1:
    aluno2 = random.randint(1, 4)
if aluno2 == aluno1:
    aluno2 = random.randint(1, 4)
else:
    if aluno2 == 1:
        print('O segundo(a) a apresentar é {}'.format(nome1))
    else:
        if aluno2 == 2:
            print('O segundo(a) a apresentar é {}'.format(nome2))
        else:
            if aluno2 == 3:
                print('O segundo(a) a apresentar é {}'.format(nome3))
            else:
                print('O segundo(a) a apresentar é {}'.format(nome4))
aluno3 = random.randint(1, 4)
if aluno3 == aluno1:
    aluno3 = random.randint(1, 4)
if aluno3 == aluno2:
    aluno3 = random.randint(1, 4)
if aluno3 == aluno1:
    aluno3 = random.randint(1, 4)
if aluno3 == aluno2:
    aluno3 = random.randint(1, 4)
if aluno3 == aluno1:
    aluno3 = random.randint(1, 4)
if aluno3 == aluno2:
    aluno3 = random.randint(1, 4)
else:
    if aluno3 == 1:
        print('O terceiro(a) a apresentar é {}'.format(nome1))
    else:
        if aluno3 == 2:
            print('O terceiro(a) a apresentar é {}'.format(nome2))
        else:
            if aluno3 == 3:
                print('O terceiro(a) a apresentar é {}'.format(nome3))
            else:
                print('O terceiro(a) a apresentar é {}'.format(nome4))
aluno4 = random.randint(1, 4)
if aluno4 == aluno1:
    aluno4 = random.randint(1, 4)
if aluno4 == aluno2:
    aluno4 = random.randint(1, 4)
if aluno4 == aluno3:
    aluno4 = random.randint(1, 4)
else:
    if aluno4 == 1:
        print('O último(a) a apresentar é {}'.format(nome1))
    else:
        if aluno4 == 2:
            print('O último(a) a apresentar é {}'.format(nome2))
        else:
            if aluno4 == 3:
                print('O último(a) a apresentar é {}'.format(nome3))
            else:
                print('O último(a) a apresentar é {}'.format(nome4))