def are_ortogonal(vect_one,vect_two):
    if len(vect_one)!=len(vect_two): #primer filto: mismo tamaño
        print("los vectores deben ser del mismo tamaño")
        return None
    else:
        for element in vect_one: #comprobamos que solo contenga números
            if type(element)!=int and type(element)!=float:
                print("los vectores solo deben contener números")
                return None
        for element in vect_two:
            if type(element)!=int and type(element)!=float:
                print("los vectores solo deben contener números")
                return None
        pdto = 0
        for i in range(len(vect_one)): #para cada índice
            pdto+=vect_one[i]*vect_two[i] #vamos sumando
        if pdto == 0: #en caso que el producto punto sea nulo
            return True #si lo son
        else:
            return False #en caso contario no
are_ortogonal([1,2],[1,4,2]) #los vectores deben tener el mismo tamaño
are_ortogonal([1,2],[1,"r"])#los vectores solo deben contener números
print(are_ortogonal([1,1],[1,-1])) #son vectores ortogonales
print(are_ortogonal([1,1],[4,3])) #no son ortogonales