# Ler os 3 lados de um triângulo e mostrar se é equilátero, isósceles ou escaleno.

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a < b+c and b < a+c and c < a+b:
    if a == b and a == c:
        print("Triângulo Equilátero")

    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")

    else:
        print("Triângulo Escaleno")

else:
    print("Os valores não podem formar um triângulo")