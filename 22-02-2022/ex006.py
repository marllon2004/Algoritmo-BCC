# Calcular se um ano é bissexto ou não.

ano = int(input("Informe o ano: "))

resto = ano % 4

if resto == 0:
    print(f'{ano} é bissexto!')

else:
    print(f'{ano} não é bissexto!')