numbers = [2,3,4,5,6,19,4,33,1]
ordered = []
def order_number_list(numbers,ascendent=True): #por defaul ordena ascendente
    ordered = []#creamos una lista para guardar lo ordenado
    if ascendent == True: #en caso ascendente
        for element in numbers:#para cada elemento
            for i in range(len(ordered)): #recorremos los índices
                if element<ordered[i]: #si se topa con algo más grande
                    ordered.insert(i,element)#insertamos en su lugar el elemento
                    break #y salimos del for
            else: #si no encuentra
                ordered.append(element) #lo añadimos al final
        return ordered
    elif ascendent==False: #en caso que sea descendente
        for element in numbers:#para cada elemento
            for i in range(len(ordered)): #recorremos los índices
                if element>=ordered[i]: #si se topa con algo más chico o igual
                    ordered.insert(i,element)#insertamos en su lugar el elemento
                    break #y salimos del for
            else:
                ordered.append(element)
        return ordered
    else:
        print("opción no válida")
        return None
print(order_number_list(numbers,False)) #si ponemos falso, será en forma descendente
print(order_number_list(numbers)) #si no lo colocamos, será ascendente