def elements_in(first_list,second_list,Common):
    if Common == True:#en caso de buscarse común
        comparative = set(first_list).difference(set(second_list)) #tomamos la lista con los elementos no en común
        for element in comparative: #recorremos elementos no en común
            first_list.remove(element) #y los eliminamos
        return first_list
    elif Common == False:
        comparative = set(first_list).intersection(set(second_list)) #en caso contrario, tomamos lo elementos en común
        print(comparative)
        for element in comparative: #los recorremos
            first_list.remove(element) #y los removemos
        return first_list
    else:
        return None
a = ["2",5,10,"verdadero"]
b = ["2","2",3,50,"falso","verdadero"]
print(elements_in(b,a,False))