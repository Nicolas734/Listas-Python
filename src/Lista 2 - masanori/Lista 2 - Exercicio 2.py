ano1 = int(input('digite o ano que deseja analisar: '))
if ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0:
          print('o {} é bissexto'.format(ano1))
else:
          print('o {} não é bissexto'.format(ano1))
