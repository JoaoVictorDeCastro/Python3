vc = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você deseja pagar?'))
vm = (anos*12)/vc
sal_30 = sal*30/100
if vm <= sal_30:
    print('Você poderá financiar!!')
else:
    print('Você não poderá concluir o empréstimo.')
