#Dever de casa
nota1 = float(input('Qual a sua nota na prova do primeiro bimestre?'))
nota2 = float(input('Qual a sua nota na prova do segundo bimestre?'))
nota3 = float(input('Qual a sua nota na prova do terceiro bimestre?'))
media = (nota1 + nota2 + nota3)/3
if media < 4:
    print('Sua nota final foi {:.2f}, por isso você foi reprovado.' .format(media))
elif 4 <= media < 7:
    print('Sua nota final foi {:.2f}, portanto você terá que fazer uma prova de recuperação' .format(media))
if  7 <= media < 10:
    print('Sua nota final foi {:.2f}, portanto foi aprovado'.format(media))
elif media == 10:
    print('Parabéns você acertou todas as questões')
#Exercício de explicação sobre estrtura de condição
num = int(input('Digite um número: '))
x = 0
while (x<=10):
    print('{} x {:2} = {:2}' .format(num, x, num*x))
    x = x+1
print('--------------------- Resultado do primeiro exercício ---------------------')
#Primeiro exercício
x = 5
while(x<=19):
    print(x)
    x = x+1
print('Fim!')
print('--------------------- Resultado do segundo exercício ---------------------')
num = int(input('Digite um número: '))
for n in range(1, 11):
    print('{} x {:2} = {:2} ' .format(num, n, num*n))