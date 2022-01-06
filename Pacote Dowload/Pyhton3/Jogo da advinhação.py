from random import randint
from time import sleep
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--')
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--')
n_USER = int(input('Em que número eu pensei?'))
print('P R O C E S S A N D O ...')
sleep(3)
n_PC = randint(1, 5)
if n_USER == n_PC:
    print('PARABÉNS! Você conseguiu me vencer.' .format(n_PC))
else:
    print('Você perdeu, o número era {} e não {}' .format(n_PC, n_USER))
