# Ler dois valores e mostrar o maior entre eles.

n1 = int(input("Informe o valor de n1: "))
n2 = int(input("Informe o valor de n2: "))

if n1 > n2:
    print(f'Maior valor é N1 --> {n1}')

elif n1 == n2:
    print(f'Valores iguais!')

else:
    print(f'Maior valor é N2 --> {n2}')