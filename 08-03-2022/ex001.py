# Elabore um algoritmo que leia um número e  calcule a soma dos número menores ou iguais a ele, começando pelo 1.

n = int(input("Informe um número: "))
i = 1
s = 0

while i <= n:
    s = s + i
    i+=1

print(f"Soma total: {s}")