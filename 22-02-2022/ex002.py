# Elabore um algoritmo que leia a idade de um nadador e determine qual categoria ele deve competir.
# Idade <= 8 anos --> Categoria INfantil A
# Idade < 13 anos --> Categoria INfantil B
# Idade < 18 anos --> Categoria Juvenil A
# Idade < 21 anos --> Categoria Juvenil B
# Idade > 21 anos --> Categoria Sênior

i = int(input("Informe a idade: "))

if i <= 8:
    print("Categoria Infantil A")

elif i < 13:
    print("Categoria Infantil B")

elif i < 18:
    print("Categoria Juvenil A")

elif i < 21:
    print("Categoria Juvenil B")

else:
    print("Categoria Sênior")
