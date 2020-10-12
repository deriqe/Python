# %%
l = int(input('Digite um valor'))
l1 = int(input('Digite outro valor'))
l2 = int(input('Digite o último valor'))
if (l + l1) > l2 and (l1 + l2) > l and (l +l2) > l1:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
