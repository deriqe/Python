# %%
import random
n = random.randint(0, 5)
nd = int(input('Tente acertar o número escolhido [Uma dica, é entre 0 e 5 ;)]'))
if nd == n: 
    print('NICE, VOCÊ ACERTOU')
else: 
    print('Desculpa bro, mas vc erro :(')
    print(f'O número certo era {n}')
