n = int(input("Informe um número: "))

s = 0

for i in range(1, n):
    if  n % i == 0:
        s += i

if s == n:
    print(f"{n} É um número perfeito!!!")
else:
    print(f"{n} NÃO é um número perfeito!!!")
