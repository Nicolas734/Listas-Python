area = int(input('tamanho da area a ser pintada: '))
lata = 54
areaporlata = area / lata
preço = areaporlata * 80
print ('quantidade de latas: ', round(areaporlata+0.5))
print (f'valor a pagar:{preço:.1f}')
