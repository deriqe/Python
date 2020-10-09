#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
# %%
frase = input(' Digite uma frase: ')
a = frase.count('A')
al = frase.find('A')
af = frase.rfind('A')
print(f'Na sua frase aparecem {a} a letra "A", sua aparição é no caracter {al} e a última no {af}')
