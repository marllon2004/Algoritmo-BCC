#Ler a distância em Km e a velocidade, e calcular o tempo de viagem.

dist = float(input("Informe a distância (Km): "))
velo = float(input("Informe a velocidade (Km/h): "))

tempo = dist / velo

print(f'O tempo de viagem é {tempo:.2f}')