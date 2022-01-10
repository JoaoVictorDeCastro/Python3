for c in range(1,11):
    print(c)
print('DESCRESCENTE')
#O último ele ignora, então se eu colocar para ele escrever de 1 até 6 eu preciso colocar o "for c in range (1,7)"
for c in range(11,0 , -1):
    print(c)
print('FIM')
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)
print('FIM')