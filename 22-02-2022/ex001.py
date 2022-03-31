# Ler o sexo e a altura de uma pessoa e mostrar o peso ideal. Homens: (72.7 * h) - 58; Mulheres: (62.1 * h) - 44.7

s = str(input("Informe o sexo (M - Masculino ou F - Feminino): ")).upper()[0]
alt = float(input("Informe a altura: "))

if s == "M":
    peso = 72.7 * alt - 58
    print(f'(M) Seu peso ideal é {peso:.2f} Kg')

elif s == "F":
    peso = 62.1 * alt - 44.7
    print(f'(F) Seu peso ideal é {peso:.2f} Kg')

else:
    print("Sexo incompatível!")