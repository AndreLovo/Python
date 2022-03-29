# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time do São Paulo.

times =('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'RB Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude')

print('==' *15)
#a) "Fatiando" a tupla
# Mostrando os 5 primeiros times:
for t in times:
 print (t)
print('==' *15)

a= times[:5]
print(f'Os cinco primeiros times são: {a}')

print('==' *15)

#b) Mostrando os quatro últimos times
b= times[-4:]
print(f'Os quatro últimos times são: {b}')

print('==' *15)

#c) Mostrando os times em ordem alfabética:
c= print(sorted(times))

#d) Mostrando a posição do São Paulo:
d=print(f'O São Paulo está na posição {times.index("São Paulo")+1}')
