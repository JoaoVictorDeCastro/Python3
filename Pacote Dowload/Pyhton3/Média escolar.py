nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1+nota2)/2
print('Tirando {} e {}, a sua média é de {:.2f} pontos.' .format(nota1, nota2, media))
if media >= 7:
    print('PARABÉNS!! Você está APROVADO.')
elif media < 5:
    print('Você está REPROVADO!')
else:
    print('Estude, ainda dá tempo. Você está de RECUPERAÇÃO.')