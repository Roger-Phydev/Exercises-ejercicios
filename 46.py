def where_is_the_robot(integer_list):
    vec = [0,0] #iniciamos una variable de coordenadas
    for i in range(len(integer_list)): #recorremos los índices
        if i%4==0: #si es múltiplo de cuatro, mira hacia arriba
            vec[1]+=integer_list[i] #se suma el número en la coordenada y
        elif i%4==1: #si es multiplo 4 más uno, mira hacia la izquierda
            vec[0]-=integer_list[i] #se resta el número en la coordenada x
        elif i%4==2: #si es dos más multiplo de 4, mira hacia abajo
            vec[1]-=integer_list[i] #se resta en la coordenada y
        else: #en el último caso, mira a la derecha
            vec[0]+=integer_list[i] #aumentamos en la coordenada x
    return vec #devolvemos el vector resultante
print(where_is_the_robot([10,5,-2])) #funciona adecuadamente
def robot(integer_list): #otra manera es esta
    vec=[0,0]
    sum_vecs = [[0,1],[-1,0],[0,-1],[1,0]] #creamos una lista con los posibles vectores
    for i in range(len(integer_list)):
        vec[0]+= sum_vecs[i%4][0]*integer_list[i] #sumamos a cada entrada, la componente adecuada del vector
        vec[1]+= sum_vecs[i%4][1]*integer_list[i] #y la multiplicamos por el correspondiente valor entero
        #lo anterior en notación vectorial es v+= int* u con u el vector adecuado, y * el producto por escalar
    return vec
print(robot([10,5,-2]))