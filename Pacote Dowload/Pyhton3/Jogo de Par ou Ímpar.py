from random import randint
print('=-'*27)
print('               VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*27)
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    while jogador < 0 or jogador > 10:
        jogador = int(input('NÚMERO INVÁLIDO. DIGITE NOVAMENTE: '))
    decisao_jogador = ''
    while decisao_jogador not in 'PI':
        decisao_jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    total = computador + jogador
    if total % 2 == 0:
        print('=-' * 27)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. DEU PAR')
        if decisao_jogador == 'P':
            print('=-' * 27)
            print('Você VENCEU')
            cont += 1
        else:
            print('=-' * 27)
            print('Você PERDEU')
            break
    if total % 2 == 1:
        print('=-' * 27)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. DEU ÍMPAR')
        if decisao_jogador == 'I':
            print('Você VENCEU')
            print('=-' * 27)
            cont += 1
        else:
            print('Você PERDEU')
            print('=-' * 27)
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
print('=-'*27)
