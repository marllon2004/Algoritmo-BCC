# Calcular a média do aluno e mostrar se foi aprovado ou não.

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (n1 + n2) / 2

print(f'Média: {media}')

if media >= 7:
    print(f'Aluno Aprovado!')
else:
    print(f'Aluno Reprovado')