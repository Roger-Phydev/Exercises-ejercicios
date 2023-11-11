def is_closed(a,b):
    if a == "(" and b == ")": #solo si los simbolos se cierran bien, entonces es verdeadero
        return True
    elif a == "[" and b == "]":
        return True
    elif a == "{" and b == "}":
        return True #de lo contrario es falso
    else:
        return False
def is_equilibrated(expresion):
    separators = [] #creamos una variable que guarde las llaves,corchetes o paréntesis que hayan
    for letter in expresion:#para cada letra en la expresión
        if letter in ["(","[","{",")","]","}"]:#si la letra coincide con un separador
            separators.append(letter) #lo agregamos a la lista
    order = [""] #colocamos eso solo para que funcione aún si inician con ],) o }
    for item in separators: #para cada elemento
        if item in ["(","[","{"]: #si el elemento abre
            order.append(item) #lo agregamos a una lista
        else: #en caso contrario
            if is_closed(order[-1],item): #vemos si cierra con el elemento anterior
                del order[-1] #eliminamos la llave abierta
            else: #en caso de que no cierre, no está equilibrada
                return False
    else:
        return True #en caso de que el for se ejecute al completo, si está equilibrada
equilibrado = "A*(B+4*[3*4-6]+2*[1+3*{6-1}])"
desequilibrado_no_cantidad = "A*(B+4*[3*4-6]+2*[1+3*{6-1}]}"
desequilibrado_mal_lugar = "a*(b+[12+4*{s+32]})"
desequilibrado_inicio = "}(23+4*5){"
desequilibrado_permutado = "[1+6*[]]"
print(is_equilibrated(equilibrado))
print(is_equilibrated(desequilibrado_no_cantidad))
print(is_equilibrated(desequilibrado_mal_lugar))
print(is_equilibrated(desequilibrado_inicio))
print(is_equilibrated(desequilibrado_permutado))
