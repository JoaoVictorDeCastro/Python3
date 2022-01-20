from random import randint
n = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue me vencer?')
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1
    if jogador == n:
        acertou = True
    else:
        if jogador < n:
            print('Mais... Tente mais uma vez.')
        elif jogador > n:
            print('Menos... Tente mais uma vez.')
print('Você acertou com {} tentativas. Parabéns!' .format(tentativas))