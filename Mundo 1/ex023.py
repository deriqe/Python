#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# %%
n = input('Digite um número entre 0 e 9999: ')
nj=(' '.join(n))
print(nj)

# %%
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')

# %%
