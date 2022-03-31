# Elaborar um programa que, considerando como dados de entrada dois valores inteiros A e B, verifique se o número B está contido entre os últimos algarismos de A.

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))

conta = 0
bb = b #Outra váriavel para armazenar o valor de B

if a >= b:
    while bb != 0:
        conta = conta + 1 #Calcula a quantidade de dígitos de B
        bb = bb // 10

    termina = a % (10**conta)

    if termina == b:
        print(f"{a} termina com {b}")
    else:
        print(f"{a} não termina com {b}")
else:
    print(f"{a} não termina com {b}")