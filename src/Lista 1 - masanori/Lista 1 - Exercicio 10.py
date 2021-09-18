cigarros = int(input('quantidade de cigarros por dia ?  '))
anos = int(input('fuma a quanto anos ?  '))
totalporano = anos * 365 * cigarros
diasportotal = totalporano / 144
print (f'{diasportotal:.1f} dias perdidos' )
