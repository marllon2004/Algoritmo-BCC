# Converter binário para decimal

n = int(input("Informe o número binário: "))

dec = 0
exp = 0

while n > 0:
    dec = dec + (n%10)*(2**exp)
    exp +=1
    n = n // 10

print(dec)