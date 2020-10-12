# %%
salario = float(input('Digite seu salário'))
if salario > 1250:
    salario = salario + salario*0.10
    print(f'Seu salário com 10% de aumento é {salario:.2f}')
else: 
    salario = salario + salario*0.15
    print(f'Seu salário com 15% de aumento é {salario:.2f}')
