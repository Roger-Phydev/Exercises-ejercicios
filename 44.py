def boomerangs_in(an_integer_list):
    if type(an_integer_list)!=list:
        print("tu entrada debe ser una lista")
        return None
    for element in an_integer_list:
        if type(element)!=int:
            print(f"debe ser una lista de puros enteros y {element} no lo es")
            return None
    if len(an_integer_list)<3:
        print("no puede haber un boomerang en tu lista, es demasiado corta")
        return None
    boomerangs = [] #creamos una lista donde irán los boomerangs
    for i in range(len(an_integer_list)-2):
        if an_integer_list[i]==an_integer_list[i+2] and an_integer_list[i]!=an_integer_list[i+1]: #si el elemento y su sucesor son diferentes, pero el siguiente a el es igual
            boomerangs.append(an_integer_list[i:i+3]) #agregamos el tramo correspondiente al boomerang
    print(f"Hay {len(boomerangs)} boomerangs en tu list") #informamos cuantos hay
    return boomerangs #y luego los devolvemos
boomerangs_in("s")
boomerangs_in([1.1])
boomerangs_in([1,3])
print(boomerangs_in([2,1,2,3,3,4,2,4]))
print(boomerangs_in([1,5,1]))