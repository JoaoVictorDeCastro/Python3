#Primeiro exercício
n = int(input('Escreva um número:'))
a = n - 1
s = n + 1
print('O antecessor é: {} ' .format(a))
print('O sucessor é: {} ' .format(s))
#Segundo exercício
n = int(input('Escreva um número:'))
d = n*2
t = n*3
q = n*n
print('O dobro é: {} ' .format(d))
print('O triplo é: {} ' .format(t))
print('O quadrado desse número é: {} ' .format(q))
#Terceiro exercício
a = float(input('Escreva a altura da sua parede em metros:'))
l = float(input('Escreva a largura da sua parede em metros:'))
area = l*a
tinta = area/2
print('A sua parede tem {:.2f} de área, portanto você precisa de {:.2f} litros de tinta' .format(area, tinta))
#Quarto exercício
preco = float(input('Quanto deu a sua compra?'))
cp = (preco/10)/2
ump = preco/100
tipo = input('Você pagará a vista ou parcelado?')
#Pagamento a vista
if tipo == 'a vista':
    preco_final= preco-(cp+(ump*3))
    print('Com o desconto o total é de R${}'.format(preco_final))
if tipo == 'A vista':
    preco_final = preco - (cp +(ump * 3))
    print('Com o desconto o total é de R${}' .format(preco_final))
#Pagamento Parcelado
if tipo == 'parcelado':
    preco_final = preco-ump*2
    parcelas = int(input('Em quantas vezes você quer dividir?'))
    preco_final = preco_final/parcelas
    print('Você pagará {} vezes de R${:.2f}.' .format(parcelas,preco_final))
if tipo == 'Parcelado':
    preco_final = preco - ump * 2
    parcelas = int(input('Em quantas vezes você quer dividir?'))
    preco_final = preco_final/parcelas
    print('Você pagará {} vezes de R${:.2f}.' .format(parcelas,preco_final))
