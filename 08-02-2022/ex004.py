# LEr dois valores A e B, e troca-los. A = B e B = A.

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))

c = a
a = b
b = c

print(f'Valor de A: {a} \n'
      f'Valor de B: {b}')