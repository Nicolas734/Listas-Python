pesopeixes = float(input('quilo de peixes sendo transportado: '))
peso = 50
if pesopeixes > peso:
          excesso = pesopeixes - peso
          multa = excesso * 4
          print('multado por valor de peso excedido')
          print('peso excedido em {:.1f} kg'.format(excesso))
          print('multa a ser paga {:.1f} reais'.format(multa))
else:
          print('peso não excedido')
          print('peso excedido: 0 kg')
          print('multa a ser paga: 0 reais')

          
