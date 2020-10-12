# %%
n = int(input('Digita um numero ai'))
n1 = int(input('Digita otro numero ai'))
n2 = int(input('Digita só mais um numero ai'))

maior = n
if n1 > n and n1 > n2:
    maior = n1
if n2 > n and n2 > n1:
    maior = n2
print(f'{maior} é o maior número digitado')

menor = n
if n1 < n and n1 < n2:
    menor = n1
if n2 < n and n2 < n1:
    menor = n2
print(f'{menor} é o menor número digitado')
