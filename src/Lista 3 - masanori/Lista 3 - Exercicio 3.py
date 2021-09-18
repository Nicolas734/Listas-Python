a=80000
b=200000
anos=0

while a<=b:
    a=(a*0.03)+a
    b=(b*0.015)+b
    anos=anos+1

print(f"{anos}anos até se igualar a população do pais B")
