#Incío das perguntas
p1 = input('Qual o nome da sua empresa?')
p2 = float(input('Quanto dinheiro vocês da(do) {} podem investir por mês?' .format(p1)))
p3 = float(input('Qual o número de funcionários que trabalham no estoque da(do) {}?' .format(p1)))
p4 = float(input('Em média, quantas toneladas de mercadorias entram no estoque da(do) {} por dia?' .format(p1)))
p5 = float(input('Em média, quantas toneladas de mercadorias você saem no estoque da(do) {} por dia?' .format(p1)))
#Guarda o resultado das perguntas e aplica em uma série de cálculos
FT = p4 + p5
N_AGV = FT/64
#Depois dos cálculos é perguntado para o usuário em quantas vezes ele deseja dividir a conta.
parcelas = int(input('Em quantas vezes você pretende dividir a sua compra?'))
#O valor total da compra é dividido pelo número de parcelas
VT = (N_AGV*160000)/parcelas
#É apresentada uma estrtura de condição que define se é possível ou não comprar os produtos necessários.
if VT > p2:
    print('Para suprir suas necessidades serão necessários {} AGVS que no total dão R${:.2f}. Seu investimento mensal não é capaz de cobrir' .format(N_AGV, VT))
else:
    print('Para suprir suas necessidades serão necessários {} AGVS que no total dão R${:.2f}. Seu investimento mensal é capaz de cobrir a compra dos nossos produtos' .format(N_AGV, VT))
    print('SERÁ UM PRAZER FAZER NEGÓCIO COM {}' .format(p1))
#FIM DO CÓDIGO

