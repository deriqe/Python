# %%
km = int(input('Quantos km tem sua viagem?'))
if km <= 200:
    p = km * 0.5
    print(f'de acordo com meus cálculos extremamente precisos e bem feitos, os gastos com essa viagem vai ser {p:.1f}')
else: 
    p = km * 0.45
    print(f'de acordo com meus cálculos extremamente precisos e bem feitos, os gastos com essa viagem vai ser {p:.1f}')
    