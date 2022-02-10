times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense',
         'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-'*300)
print(f'Lista de times do Brasileirão: {times}')
print('-'*300)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('-'*300)
print(f'Os quatro últimos são: {times[-4:]}')
print('-'*300)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-'*300)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
print('-'*300)
