#El caso del quick sort es uno interesante. Tenemos delante, un algoritmo en donde dado una lista, la iremos partiendo para poder ordenarla de forma rápid
def partition(a_list,low,high): #primero creamos la función que hara la partición
    pivot = a_list[high] #tomamos un pivote en el extremo derecho
    i = low-1 #este será un puntero para el primer elemento más grande que el pivote
    for j in range(low,high):#recorremos toda la partición
        if a_list[j]<= pivot:#si se encuentra un elemento que no sea más grande que el pivote
            i+=1 #avanzamos uno, pues el anterior ya sabemos que no es más grande que el pivote
            (a_list[i],a_list[j])=(a_list[j],a_list[i]) #luego intercambiamos de posición el i con el j, poniendo lo más grande a la derecha
            print(a_list)
    (a_list[i+1],a_list[high])=(a_list[high],a_list[i+1]) #finalmente, intercambiamos el más grande con el pivote quedando lo siguiente:
    # menores iguales a pivot,pivote,mayores que pivote
    print(a_list)
    return i+1 #regresamos el valor después de i+1, pues en i+1 ahora está el pivote.
def quick_sort(array,low,high): #ahora si el ordenamiento rápido
    if low<high: #si se tienen los números adecuados
        pi = partition(array,low,high) #pi será el índice del pivote después ordenar esta partición en [<piv,piv,>piv]
        #aqui viene la parte iterativa, aplicaremos este método
        print(pi,array[low:pi],array[pi],array[pi+1:high+1])
        quick_sort(array,low,pi-1) #ahora aplicamos lo mismo para la parte para los elementos por debajo
        quick_sort(array,pi+1,high) #y luego para los de arriba
a = [1,7,4,1,10,9,-2]
print(a)
partition(a,0,6) #en este caso, como el pivote es el -2, no hay elementos por debajo, asi que solo aplica la l+inea antepenultima, lo manda al inicio
print(partition(a,0,0)) #si low=high, develve low
print("////////////////////////////////////////////")
quick_sort(a,0,6) #Aqui debe considerarse que previamente ya acomodamos el -2, por la línea 32, así, la lista de acciones son:
# 1.- acomoda el 1, así, los elementos que quedan a la izquierda son -2 y 1(pues -2,1<=1)
# 2.- ahora el conjunto queda separado en dos: [-2,1] y [7,10,9,4]
# 3.- al aplicar esto a [-2,1] no aplica cambios, al ya estar ordenado no lo afecta y se hace aquí pi=0, por lo que deja de ejecutarse (pues range(0,-1) y range(1,0) no se ejecutan)
# 4.- al aplicar a [7,10,9,4], coloca el 4 como sigue [4,10,9,7] al no haber menores o iguales a 4, generando solo una lista por encima: [10,9,7]
# 5.- [10,9,7] se ordena de acuerdo al 7 solo en una superior: [10,9]
# 6.- por último ordena este en [9,10] y con eso concluye
#básicamente el funcionamiento es mejor explicado pictóricamente, por ello se tienen los print y la explicación