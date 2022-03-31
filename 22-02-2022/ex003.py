# Desconto de 25% se o valor da compra for maior ou igual a r$ 500.00, 20% se for maior ou igual a r$ 200.00 e menor que r$ 500.00, e 15% caso seja menor que r$200.00.

compra = float(input("Informe o valor da compra: "))

if compra >= 500:
    desconto = compra * 0.25
    compra2 = compra - desconto

elif compra >= 200 and compra < 500:
    desconto = compra * 0.20
    compra2 = compra - desconto

else:
    desconto = compra * 0.15
    compra2 = compra - desconto

print(f'Valor da compra: {compra} \n'
      f'Valor do desconto: {desconto} \n'
      f'Valor a ser pago: {compra2}')