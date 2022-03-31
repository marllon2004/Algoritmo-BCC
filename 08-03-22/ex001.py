# Elabore um algoritmo que leia um número e calcule a soma dos números menores ou iguais a ele, começando pelo 1.

n = int(input("Informe um número: "))

i = 1
soma = 0

while i <= n:
    soma = soma + i

    i+=1

print(soma)