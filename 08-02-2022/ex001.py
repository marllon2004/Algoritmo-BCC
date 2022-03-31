#Ler o salário de um funcionário, o total valor das vendas e mostrar o novo salário com a comissão de 4%.

salario = float(input("Informe o salário: "))
vendas = float(input("Informe o valor total das vendas: "))

comissao = vendas * 0.4
n_salario = salario + comissao

print(f'Salário Antigo: {salario} \n'
      f'Comissão: {comissao} \n'
      f'Novo Salário: {n_salario}')
