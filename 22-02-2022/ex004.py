# Calcular o IMC. IMC = Peso / altura^2
# < 18 --> Abaixo do peso
# >= 18 e  < 25 --> Peso normal
# >= 25 e < 30 --> Acima do peso
# >= 30 --> Obesidade

peso = float(input("Informe o peso: "))
alt = float(input("Informe a altura: "))

imc = peso / (alt ** 2)

if imc < 18:
    print(f'IMC: {imc:.2f} \nAbaixo do Peso')

elif imc < 25:
    print(f'IMC: {imc:.2f} \nPeso Normal')

elif imc < 30:
    print(f'IMC: {imc:.2f} \nAcima do Peso')

else:
    print(f'IMC: {imc:.2f} \nObesidade')