# %%
a = input('Digite algo: ')
print('O tipo primitivo do texto digitado é: ', type(a))
print('Pode ser convertido em número:', a.isnumeric())
print('Pode ser convertido em texto: ', a.isalpha())
print('Pode ser convertido em número ou texto:', a.isalnum())
