def fact(n):
    if n<0:#en este caso no hay factorial
        return None
    elif n<=1:
        return 1 #en caso de 0 y 1 el factorial es 1
    else: 
        return n * fact(n-1)#esta es la parte recursiva
print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))