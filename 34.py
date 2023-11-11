def format_list(a_list):
    if type(a_list)!=list: #en caso que no sea una lista
        print("el argumento debe ser una lista")
        return (False,0)
    for element in a_list:
        if type(element)!=int:#si por lo menos un elemento no es entero
            print("las entradas de tu lista deben ser enteros")
            return (False,0)#devuelve falso
    if len(set(a_list))==len(a_list): #si la lista al quitar repeticiones sigue teniendo la misma cantidad (no hay repetidos)
        ascent = a_list.copy()#creamos copias de la lista ordenadas de forma ascendento o descendente
        ascent.sort() #ordenada ascendente
        descent = list(reversed(ascent)) #el otro es ascendente revertido
        if a_list==ascent: #si la lista coincide con la ascendente
            return (True,1) #es correcto y usamos el uno para señalar ascendente
        elif a_list==descent: #si concuerda con la descendente
            return (True,-1) #es correcto y usamos el menos uno para señalar descendente
        else:#en caso contrario
            print("Tu lista debe estar ordenada")
            return (False,0)
    else:
        print("tu lista no debe tener repetidos")
        return (False,0)
def missed_numbers_in(numbers_list):
    char = format_list(numbers_list)#vemos si el formato es correcto
    lacked = [] #aqui guardamos los faltantes
    if char[0]==True and char[1]==1:
        for i in range(numbers_list[0],numbers_list[-1]): #empezamos por el mínimo y terminamos en el máximo, que son los extremos al estar ordenada
            if i not in numbers_list:
                lacked.append(i)
        return lacked
    elif char[0]==True and char[1]==-1:
        for i in range(numbers_list[-1],numbers_list[0]): #solo volteamos los argumentos
            if i not in numbers_list:
                lacked.append(i)
        return lacked
print(missed_numbers_in([0,101])) #con esta función también podemos contar hasta 100
n_one = [1,3,9,10]
n_two = [10,9,2,1]
n_three = [1,3,2]
n_four = [1,1,3,4]
n_five = [1.2,3,4,"f"]
n_six = "right"
print(missed_numbers_in(n_one)) #aquí es ascendente
print(missed_numbers_in(n_two)) #aquí es decendente
missed_numbers_in(n_three) #aquí no están ordenados
missed_numbers_in(n_four) #aquí hay repetidos
missed_numbers_in(n_five) #aquí no son enteros todos
missed_numbers_in(n_six) #aquí no es una lista