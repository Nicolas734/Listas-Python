n1 = int (input('Digite o primeiro numero: '))
n2 = int (input('Digite o segundo numero: '))

while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
print (f'O MDC dos seus números é: {n2}')
