# Ler a velocidade de um carro e a velocidade permitido. E verificar se o carro levará multa ou não.

velo = float(input("Velocidade permitida: "))
velo_car = float(input("Velocidade do carro: "))

if velo_car > velo:
    print(f'Velocidade acima da permitida! Motorista multado!')

else:
    print(f'Velocidade nos conformes! Motorista não multado!')
