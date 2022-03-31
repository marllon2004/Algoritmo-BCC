#Ler um valor em reais (R$) e mostrar a conversão para dólar ($).

reais = float(input("Informe o valor em reais: R$ "))
dolar = float(input("Informe a cotação do dólar: $ "))

conversao = reais / dolar

print(f'R$ {reais} reais para Dólar é $ {conversao} dólares')