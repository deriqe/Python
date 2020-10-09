# %%
from math import sqrt, hypot
ca = int(input('Digite o valor do cateto adjacente: '))
co = int(input('Digite o valor do cateto oposto: '))
a = hypot(ca, co)
print(f'O valor da hipotenusa é {a}')
