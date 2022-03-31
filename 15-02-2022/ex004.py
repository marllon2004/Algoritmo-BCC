# Ler 3 valores e mostrar o maior entre eles.

n1 = int(input("Informe o valor de N1: "))
n2 = int(input("Informe o valor de N2: "))
n3 = int(input("Informe o valor de N3: "))

if n1 == n2 or n1 == n3 or n2 == n3:
    print(f'Valores Iguais!')

elif n1 > n2 and n1 > n3:
    print(f'N1 é o maior valor. ({n1})')

elif n2 > n1 and n2 > n3:
    print(f'N2 é o maior valor. ({n2})')

else:
    print(f'N3 é o maior valor. ({n3})')