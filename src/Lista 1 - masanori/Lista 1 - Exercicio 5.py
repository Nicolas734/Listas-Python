mercadoria = float(input( 'Digite o valor da mercadoria: ' ))
desconto = int(input( 'Digite o valor do desconto: ' ))
valorfinal =  desconto*mercadoria / 100 - mercadoria
valorfinalpositivo = valorfinal * (-1)
descontovalor = desconto*mercadoria / 100 + mercadoria
valordodesconto = descontovalor - mercadoria
print (f' valor: {valorfinalpositivo} ')
print (f' valor descontado: {valordodesconto} ')
