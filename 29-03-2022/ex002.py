n = int(input("Informe o número para saber o Fatorial: "))
fat = 1

for i in range(n):
    fat = fat * (n-i)

print(f"Fatorial de {n} é {fat}")