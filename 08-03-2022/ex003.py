# Considerando uma classe com 60 alunos, elabore um algoritmo que leia duas notas de cada aluno, calcule a média e verifique se aluno foi aprovado ou reprovado. Para estar aprovado a média deverá ser maior ou igual a 6. Determine também a média geral da classe e a quantidade de alunos aprovados e reprovados da turma.

n = int(input("Informe a quantidade de alunos: "))

i = 1
aAprovados = 0
aReprovados = 0
mediaGeral = 0

while i <= n:
    n1 = float(input("Informe a 1º nota: "))
    n2 = float(input("Informe a 2º nota: "))

    media = (n1+n2)/2
    mediaGeral = mediaGeral + media

    if media >= 6:
        print(f"Média {media} --> Aluno Aprovado!\n")
        aAprovados += 1

    else:
        print(f"Média {media} --> Aluno Reprovado!\n")
        aReprovados += 1

    i+=1

print(f"Média Geral --> {mediaGeral / n:.2f} \n"
      f"Alunos Aprovados --> {aAprovados} \n"
      f"Alunos Reprovados --> {aReprovados}")