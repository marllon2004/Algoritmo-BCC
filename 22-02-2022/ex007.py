# Ler A, B C. Coloca-los em ordem crescente com C -> maior | B -> Meio | A -> Menor

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

if a <= c and c <= b:
    aux = c
    c = b
    b = aux

elif b <= a and a <= c:
    aux = b
    b = a
    a = aux

elif b <= c and c <= a:
    aux = c
    c = a
    a = b
    b = aux

elif c <=a and a<= b:
    aux = c
    c = b
    b = a
    a = aux

elif c <= b and b < a:
    aux = c
    c = a
    a = aux

print(f'Maior, C: {c} \n'
      f'Meio, B: {b} \n'
      f'Menor, A: {a}')