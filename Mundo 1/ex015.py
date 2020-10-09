# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

# %%
km = float(input(' Digite os km rodads: '))
d = int(input(' Digite quantos dias foi alugado: '))
kmp = km * 0.15
dp = d * 60
print(f'O preço ficou {kmp+dp} reais')
