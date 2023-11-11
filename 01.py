for n in range(1,101): #pasamos por todos los números del 1 al 100
    if n%3==0 and n%5==0: #si tanto 3 como 5 lo dividen
        print("fizzbuzz")
    elif n%3==0: #si no lo dividen ambos, vemos si lo divide el 3
        print("fizz")
    elif n%5==0: #si tampoco lo divide 3, vemos si lo divide el 5
        print("buzz")
    else: #si no ocurre ninguno de los anteriores
        print(n) #imprime el número