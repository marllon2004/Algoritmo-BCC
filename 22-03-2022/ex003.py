# Elabore um algoritmo, que simule um Caixa de supermercado. Para isso, leia preos e a quantidade comprada de cada produto. Calcule e mostre o total que o cliente gastou em sua compra. Encerrar o algoritmo quando for digitado 0 para o preço.
total = 0

while True:
    preco = float(input("Informe o preço do produto: "))

    if preco == 0:
        break

    quant = int(input("Informe a quantidade do produto comprado: "))

    total = total + (preco * quant)


print(f"O total da compra é: {total}")