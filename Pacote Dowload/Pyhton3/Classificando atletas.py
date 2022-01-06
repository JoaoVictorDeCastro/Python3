from datetime import date
ano = int(input('Qual seu ano de nascimento?'))
idade = date.today().year - ano
if idade <= 9:
    print('MIRIM é a categoria para pessoas de {} anos.' .format(idade))
elif idade > 9 and idade <= 14:
    print('INFANTIL é a categoria para pessoas de {} anos.' .format(idade))
elif idade > 14 and idade <= 19:
    print('JUNIOR é a categoria para pessoas de {} anos.' .format(idade))
elif idade > 19 and idade <= 25:
    print('SÊNIOR é a categoria para pessoas de {} anos.' .format(idade))
elif idade > 25:
    print('MASTER é a categoria para pessoas de {} anos' .format(idade))
