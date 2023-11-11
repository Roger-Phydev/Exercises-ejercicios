def dec_to_bin(number):
    r=[] #inicializamos esta variable
    while number>=1: #mientras el número no sea menor a 1
        r.append(int(number%2)) #calculamos el residuo y lo guardamos de forma entera
        number = (number - number%2)/2 #restamos el residuo y lo dividimos entre 2
    r.reverse() #invertimos la lista
    for l in r:
        print(l,end="") #imprimimos los elementos de corrido
    print("") #damos salto de linea
dec_to_bin(19)

