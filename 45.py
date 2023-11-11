#Para empezar crearemos una función que devuelva los subdepositos de la lista, pues solo las casillas en ellos contribuyen a el agua
#para que haya un subdeposito, debe tenerse una cadena ascendente después de una bajada. Es decir:
# si empezamos con 4 a la derecha debe haber un 3 o menos, luego a la derecha de ese 3 debe haber un 3 o más y así sucesivamente
# si en vez de hay menos de un 3 al lado del anterior 3, el 3 cerraría un subdeposito, y abriría otro
# además, a la derecha del 4 no puede haber otro 4, pues estaría al mismo nivel y no habría sub depósito
def sub_depots(a_list):
    i=0#creamos una variable para saber donde acaban los subdepositos
    j=1 #un cursor para ir recorriendo
    subs = [] #una lista que contendrá las parejas de indices de inicio y fin de cada deposito
    while i<len(a_list)-1: #mientras no rebase la lista
        if a_list[i]>a_list[j]: #si hay una bajada, inicia un deposito            
            if j < len(a_list): #si j no ha arrebasado el máximo
                while a_list[i]>a_list[j]: #mientras siga estándo debajo del inicio
                    if j <len(a_list)-1: #mientras no llegue al máximo
                        j+=1 #aumentamos el valor de j
                    else: #en caso que llegue al máximo
                        break #nos salimos del bucle
                subs.append((i,j)) #añadimos el subdeposito que inicia en start y acaba en i
                i=j #ahora iniciamos en j
                j+=1 #y nos movemos uno a la derecha
        else: #en caso de no cumplirse la condición
            i+=1 #nos recorremos uno a la derecha
            j+=1
    return subs
#probamos que en verdad regrese lo que buscamos
print(sub_depots([3,1,4,1,7,8,8,1,1,4,4]))
proof = [4,0,3,6,1,3]
print(sub_depots(proof))
def water_between(a_list):
    depots = sub_depots(a_list) #creamos una lista de subdepositos
    water = 0 #creamos una variable de agua
    for depot in depots:#para cada deposito
        m = min(a_list[depot[0]],a_list[depot[1]]) #nos fijamos cual columna del extremo del deposito es la más chica
        for i in range(depot[0]+1,depot[1]): #nos fijamos en los indices entre los extremos del deposito
            if a_list[i]<m:
                water+=m-a_list[i] #solo para las columnas más pequeñas que la más pequeña de los extremos se suman cuadros de agua
                #esto hace que por ejemplo [8,4,4] no contenga agua
    return water #regresamos el valor
print(water_between(proof)) #verificamos que funciones
print(water_between([6,6,1,3,1,9]))
print(water_between([3,1,2,1,3]))
print(water_between([5,1,3,1,7]))