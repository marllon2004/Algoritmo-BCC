# Elabore um algoritmo para mostrar a tabuada de um número N qualquer lido pelo teclado.

n = int(input("Informe o número da tabuada: "))
i = 1

while i <= 10:
    tabu = n * i
    print(f"{n} x {i} = {tabu}")
    i+=1
