# Elabore um algoritmo que leia idades de um grupo de pessoas e, calcule e mostre a média das idades lidas. O algoritmo deverá ser encerrado quando idade lida for zero (0)

media = 0
c = 0

while True:
    c += 1
    idade = int(input(f"Informe a idade da {c}º pessoa ou [0] para encerrar o programa: "))
    media += idade

    if media == 0:
        print("Não há média!!")
        break

    elif idade == 0:
        print(f"A média das idades é: {media / (c-1):.2f}")
        break
