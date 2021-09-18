nota = int(input('digite uma nota de 0 a 10:  '))
while ( nota > 10 ):
    print ( 'tente novamente' )
    nota = int(input('digite um numero de 1 a 10 '))
if (nota < 10 ):
    print ('muito bem')
