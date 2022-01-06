velocidade = float(input('Qual a velocidade atual do seu carro?'))
if velocidade > 80:
    multa = (velocidade-80)*7
    print('MULTADO! A velocidade limite é 80km/h')
    print('Você deve pagar uma multa de R${:.2f}' .format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
print('Tenha um bom dia! Dirija com segurança!')