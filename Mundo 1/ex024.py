#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
# %%
city = input('Digite o nome de uma cidade')
cl = city.lower()
cs = cl.split()
c = cs[0] == 'santos'
if c == True:
    print('Sua cidade começa com "santos"')
else: 
    print('Sua cidade não começa com "santos"')
