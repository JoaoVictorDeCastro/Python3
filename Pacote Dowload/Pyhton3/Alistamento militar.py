from datetime import date
nasc = int(input('Digite seu ano de nascimento:'))
ano = date.today().year
alist = ano - nasc
print('Quem nasceu em {} tem {} anos  em {}' .format(nasc, alist, ano))
if alist > 18:
    dif = alist - 18
    print('Você deveria ter se alistado há {} anos.' .format(dif))
    print('Seu alistamento foi em {}' .format(ano-dif))
elif alist == 18:
    print('Você deve se alistar esse ano.')
elif alist < 18:
    dif = 18 - alist
    print('Você deverá se daqui a {} anos.' .format(dif))
    print('Seu alistamento será em {}' .format(ano+dif))