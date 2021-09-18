n0 = int(input('digite a posição desejada da sequencia de fibonacci: '))
n1 = 0
n2 = 1
n3 = 0

print('sequencia de fibonacci')

while n3 < n0:
    n = n1 + n2
    n1 = n2
    n2 = n
    n3 += 1
if n3 == n0:
    print ( n1 )
