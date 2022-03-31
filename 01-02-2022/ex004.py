#Ler o preço de um produto e mostrar o novo preço com 10% de desconto.

preco = float(input("Informe o preço do produto: "))

n_preco = preco - (preco * 0.10)

print(f'Preço anitgo: {preco} \n'
      f'Novo Preço com desconto de 10%: {n_preco}')
