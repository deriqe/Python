#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# %%
nome = (input(' Digite seu nome completo: ')).strip()
ns=(nome.split())
print(f'Seu primeiro nome é {ns[0]}, e o último é {ns[-1]}')

# %%
