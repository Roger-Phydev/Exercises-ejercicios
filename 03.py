a=0
b=1
c=0
print(f"{a}\n{b}") #imprimimos los primeros dos valores
for i in range(48): #para los restantes aplicamos iteraciones
    c=a+b
    a=b
    b=c
    print(c)