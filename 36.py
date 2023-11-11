def who_will_win_battle(members_of_light_list,members_of_dark_list):
    light_values = [1,2,3,4,5] #creamos listas con el valor de cada elemento en orden
    dark_values = [-2,-2,-2,-3,-5]
    if type(members_of_dark_list)!=list or type(members_of_light_list)!=list: #si no son listas lo informamos
        print("error, las entradas deben ser listas")
        return None
    if len(members_of_dark_list)!=5 or len(members_of_light_list)!=5: #si no tienen la longitud adecuada informamos
        print("error, las listas deben contener solo 5 elementos")
        return None
    for element in members_of_light_list:
        if type(element)!=int:
            print("error, en tu lista de la luz solo deben haber enteros positivos")
            print("La lista indica lo siguiente [# de pelosos,#de sureños buenos,#enanos,#númenóreanos,#elfos]")
            return None
    for element in members_of_dark_list:
        if type(element)!=int:
            print("error, en tu lista de la oscuridad solo deben haber enteros positivos")
            print("La lista indica lo siguiente [# sueños malos,#orcos,#goblins,#huargos,#trolls]")
            return None
    s = 0 #nos servirá para saber quien gana
    for i in range(10): #recorremos los índices 0 al 4 dos veces
        if i<5: #para los primeros cinco índices
            s+=members_of_light_list[i]*light_values[i] #aumentamos según la lista de valores de la luz
        else:
            s+=members_of_dark_list[i%5]*dark_values[i%5] #aumentamos según la lista de valores de la oscuridad
    if s>0:#segúns sea el caso señalamos quien gana
        return "light wins"
    elif s == 0:
        return "Tie"
    else:
        return "Dark wins"
who_will_win_battle("elfo",[1,1,1,1,1]) #alguno no es lista
who_will_win_battle([1,1,1,1,1,1],[0,1]) #no tienen el tamaño adecuado
who_will_win_battle([1,1,1,1,2.5],[1,1,1,1,1])#no tienen números enteros 
print(who_will_win_battle([1,1,1,1,1],[1,1,1,1,1])) #gana la luz
print(who_will_win_battle([0,0,0,0,1],[0,0,0,0,1])) #empatan
print(who_will_win_battle([1,0,0,0,1],[1,0,0,0,1])) #gana la oscuridad