#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# %%
nome = input('Digite o seu nome: ')
n = nome.lower()
s = 'silva' in n
if s == True:
    print('Tem silva no seu nome')
else: 
    print('Não tem silva no seu nome')
