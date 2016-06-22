dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos  = int(input('Segundos: '))

total = dias * 24 * (60 ** 2) + horas * (60**2) + minutos * 60 + segundos
print('O total em segundos é: %ds' %total)
