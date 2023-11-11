def is_prime(n): #creamos nuestra función
    div = 2 #buscaremos un divisor mayor a 1
    while n%div !=0 and div<n//2: # mientras este no divida a n y solo buscamos hasta la mitad de n, pues los demás no serán divisores
        div+=1#aumentamos su valor
    if div == n//2: #si no se encuentra un divisor hasta n//2 (esto se hace para reducir tiempo y cálculos)
        return True
    else:
        return False #en caso contrario, no será primo
for i in range(1,101): #para los números del 1 al 100
    if is_prime(i):#si es primo
        print(i)#lo imprime