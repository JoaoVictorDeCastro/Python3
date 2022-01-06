percurso = float(input('Qual a distância em Km da sua viagem?'))
if percurso <= 200:
    print('O preço da sua passagem será R${:.2f}' .format(percurso*0.5))
else:
    print('O preço da sua passagem será R${:.2f}' .format(percurso*0.45))
