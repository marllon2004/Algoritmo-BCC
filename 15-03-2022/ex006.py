# Converter decimal para binário

n = int(input("Informe o número decimal: "))

bi = 0
fator = 1

while n > 0:
    bi = bi + fator * (n%2)
    fator *= 10
    n //= 2

print(bi)