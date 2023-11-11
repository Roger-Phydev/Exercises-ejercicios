#aquí vamos a usar un fichero de tipo txt que tenga operaciones y nosotros regresaremos su cálculo
import re
def format(an_string):#creamos una función para comprobar el formato de cada línea
    patron_int = r"[0-9]+$" #usaremos este patrón:uno o más cifras, un punto y uno o más cifras decimales y acaba, o bien, una o más cifras y acaba
    patron_float = r"[0-9]+.[0-9]+$"
    if an_string in ["+","-","*","/"]:
        return "operation" #devuelve que es operación
    elif re.match(patron_int,an_string)!=None: #si concuerda con el patrón
        return "int number" #devuelve que es número
    elif re.match(patron_float,an_string)!=None:
        return "float number"
    else: #en caso que ni sea el patrón, o sea un símbolo
        return "no match" #devuelve nada
def format_list(a_list): #creamos una función que compruebe el formato de la lista de caracateres, convirtiendo de paso sus entradas adecuadamente
    if len(a_list)%2 == 0:
        return False#si tiene longitud par, no puede tener el formato adecuado
    else: #en caso que no tenga esta longitud
        for i in range(len(a_list)): #recorremos el índice
            if i%2 == 0: #si es una entrada par: 0,2,...
                if format(a_list[i]) not in ["int number","float number"]: #y el formato no es un número
                    return False #regresamos falso
            else: #si la entrada es impar: 1,3,...
                if format(a_list[i]) != "operation": #y el formato no es una operación
                    return False #regresamos falso
            #una vez pasados los filtros, vamos convirtiendo datos adecuadamente para luego operar con nuestra función previa
            if format(a_list[i]) == "float number": #si el formato es float
                a_list[i] = float(a_list[i]) #convertimos el dato a float
            elif format(a_list[i]) == "int number": #si el formato es int
                a_list[i] = int(a_list[i]) #convertimos el dato a int
        return True #en caso que pase todos los filtros, regresamos True
def operate_two_numbers_with_op(number_one,number_two,op): #esta función opera números con una operación
    if op == "+": #luego, si tiene el formato, devolvemos la operación
        return number_one + number_two
    elif op == "-":
        return number_one - number_two
    elif op == "*":
        return number_one * number_two
    elif op == "/":
        return number_one / number_two
    else:
        return "syntax error" #damos un formato parecido a una calculadora en caso de error
###########################################################################################################################################################
#aquí inicia el programa
with open("operaciones_calc.txt","r") as archivo: #abrimos el archivo
    entradas = archivo.readlines() #guardamos cada línea en una lista
    for i in range(len(entradas)): #para cada elemento de la lista
        entradas[i] = entradas[i].strip() #quitamos los saltos de línea
    if format_list(entradas): #si cumple el formato...
        Total = entradas[0] #iniciamos esta variable, que será un número por el formato exigido
        if len(entradas)==1:#si solo contiene un número
            print(Total) #regresamos ese valor
        else:#en caso de que sean más
            for i in range(1,len(entradas)-1,2): #para cada índice, va desde 1 hasta donde llegue menos dos, tomando de dos en dos elementos
                print(f"{Total} {entradas[i]} {entradas[i+1]} = ",end="") #imprimimos la operación, sin saltar de línea
                Total = operate_two_numbers_with_op(Total,entradas[i+1],entradas[i])
                #el total es la operación indicada en la entrada i del total con el siguiente número
                print(f"{Total}") #imprimimos el total nuevo, y saltamos de línea
    else:
        print("tu archivo no cumple el formato, revisa que:")
        print("-Solo contiene un número o una operación en cada renglón")
        print("-Las operaciones que usas son las siguientes: + - * /")