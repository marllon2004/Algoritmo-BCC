# Elabore um algoritmo para resolver uma operação aritmética escolhida pelo usuário. Para isto, leia operador (+, *, -, / ou #). O caractere # será usado para encerrar o programa. Em seguida, leia dois operandos (números reais). O algoritmo deverá realizar a operação escolhida entre os valores lidos.

while True:
    n1 = int(input("Informe um número: "))
    n2 = int(input("Informe outro número: "))
    op = input("Informe um operador (+, -, *, / ou # para encerrar o programa: )")

    if op == "+":
        resu = n1 + n2
    elif op == "-":
        resu = n1 - n2
    elif op == "*":
        resu = n1 * n2
    elif op == "/":
        resu = n1 / n2
    elif op == "#":
        break
    print(resu)