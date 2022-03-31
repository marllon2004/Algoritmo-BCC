# Converter segundos em horas, minutos e segundos.

tempo = int(input("Informe o tempo ems egundos: "))

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = (tempo % 3600) % 60

print(f'Horas: {horas} \n'
      f'Minutos: {minutos} \n'
      f'Segundos: {segundos}')