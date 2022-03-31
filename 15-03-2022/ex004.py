# Elabore um algoritmo que leia um número inteiro e determine quantos algarismos ele possui

n = int(input("informe um número: "))

c = 0

if n == 0:
    c = 1

else:
    while n != 0:
        c+=1
        n = n // 10

print(c)