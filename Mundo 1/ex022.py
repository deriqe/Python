#022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas. 
# - Quantas letras ao todo (sem considerar espaços). 
# - Quantas letras tem o primeiro nome.
# %%
nome = (input(' Digite seu nome completo: '))
ns=(nome.split())
nj=(''.join(ns))
print(f'Seu nome com todas as letras maiúsculas fica "{nome.upper()}", e com todas minúsculas fica "{nome.lower()}"')
print(f'Seu nome tem {len(nj)} letras')
print(f'Seu primeiro nome tem {len(ns[0])} letras')
