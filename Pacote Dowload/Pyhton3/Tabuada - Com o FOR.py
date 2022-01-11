n = int(input('Você deseja saber a tabuada de qual número?'))
for tabuada in range(0, 11):
    num = n*tabuada
    print('{} x {} = {}'.format(n, tabuada, num))