dias = int(input('quantidade de dias: '))
horas = int(input('quantidade de horas: '))
minutos = int(input('quantidade de minutos: '))
segundo = int(input('quantidade de segundos: '))

d = 86400
ds = d * dias

h = 3600
hs = h * horas

m = 60
ms = m * minutos

dhms = ds + hs + ms + segundo

print (f' {dhms} segundos')
