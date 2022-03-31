# Elabore um algoritmo que leia  uma nota. Caso uma nota lida seja inválida, emitir mensagem e repetir a entrada de dados.

while True:
    n = int(input("Informe uma nota: "))

    if (n < 0) or (n > 10):
        print(f"[ERROR]\nA nota {n} não pode ser menor que 0 ou maior que 10!!!\n")
    else:
        print("Nota válida!!!")
        break
