# %%
import random
name = input('Digite o nome do aluno: ')
name1 = input('Digite o nome do aluno: ')
name2 = input('Digite o nome do aluno: ')
name3 = input('Digite o nome do aluno: ')
alunos = [name, name1, name2, name3]
esc = random.sample(alunos, 4)
print(f'A ordem ficou {esc}')

# %%
