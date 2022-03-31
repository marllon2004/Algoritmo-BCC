# Ler o comprimento e a largura de um terreno retangular e mostrar o perímetro e a área.

comp = float(input("Informe o  comprimento: "))
larg = float(input("Informe a largura: "))

perimetro = 2 * (comp + larg)
area = comp * larg

print(f'O Perímetro é {perimetro} \n'
      f'A área é {area}')