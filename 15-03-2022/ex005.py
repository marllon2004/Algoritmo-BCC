# Elabore um algoritmo que leia um número inteiro e o inverta

n = int(input("Informe um número: "))

i = 0

while n != 0:
    resto = n % 10
    i = i * 10 + resto
    n = n // 10

print(i)