# Un número de Armstrong es aquel en donde N = a_{n}a_{n-1}...a_{1} donde a_{i} es una cifra del número (note que n es el número de cifras).
# entonces este cumple que N = a_{n}^n + a_{n-1}^n + ... + a_{1}^n
def is_armstrong(Natural):
    T = 0 #aqui guardamos lo que sumen las cifras
    Natural = str(Natural) #convertimos a string
    n = len(Natural) #para poder calcular fácilmente el número de cifras
    for i in range(n): #recorriendo las cifras
        T+= (int(Natural[i]))**n #sumamos la i-ésima cifra elevada a la n
    Natural = int(Natural) #después de aprovechar su uso como str lo reconvertimos a entero
    print(Natural,T)
    if T == Natural: #para poder compararlo y ver si es un número de armstrong o no
        return True
    else:
        return False
a = 371
b = 8208
c = 4210818
d = 865
print(is_armstrong(a))
print(is_armstrong(b))
print(is_armstrong(c))
print(is_armstrong(d))