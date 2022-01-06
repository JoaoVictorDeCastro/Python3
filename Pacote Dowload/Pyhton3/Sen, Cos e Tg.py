from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo:'))
seno = sin(radians(angulo))
print('O SENO de {} é: {:.2f}' .format(angulo, seno))
cosseno = cos(radians(angulo))
print('O COSSENO de {} é: {:.2f}' .format(angulo, cosseno))
tg = tan(radians(angulo))
print('A TANGENTE de {} é: {:.2f}' .format(angulo, tg))
