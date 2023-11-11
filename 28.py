def change_of(bill,number_of_each_list,coins_list,name):
    for i in range(len(coins_list)): #primero vemos que las entradas sean números enteros positivos en cada lista
        if type(coins_list[i])!=int or coins_list[i]<=0:
            print("la lista de monedas admitida debe contener solo números enteros positivos")
            return None
        elif i>0 and coins_list[i-1]<=coins_list[i]:
            print("la lista de monedas debe ser descendente")
            return None
    for number in number_of_each_list:
        if type(number)!= int or number<0:
            print("las cantidades de cada moneda no deben ser enteros negativos")
            return None
    if type(bill)!=int or bill<=0:
        print("la cuanta a cobrar debe ser un entero positivo")
        return None
    if len(number_of_each_list)!=len(coins_list):
        print("Alguna moneda no concuerda con los valores")
        return None
    receive = 0 #tendremos lo que nos entregan
    for i in range(len(number_of_each_list)): #para cada indice
        receive+=number_of_each_list[i]*coins_list[i] #sumamos la cantidad de monedas multiplacado por el valor de la moneda
    if bill>receive: #en caso de dinero insuficiente
        print("dinero insuficiente") #lo señalamos
        return number_of_each_list #devolvemos lo mismo que metieron a la máquina
    elif bill==receive:
        print(name)#imprime el nombre del producto
        return [] #en caso de que sea exacto, no regresamos nada
    else:
        print(name) #señalamos el nombre
        change = [] #creamos la lista de cambio
        diff = receive - bill #consideramos la diferencia
        for coin in coins_list:
            if diff//coin == 0: #en caso que la moneda sea más grande
                change.append(0) #se agrega un cero
            else:
                change.append(diff//coin) #agregamos la máxima cantidad de monedas
                diff = diff%coin #y ahora la diferencia será solo el residuo
        return change 
def vendor_machine(list_of_coins_numbers,selection):
    if selection==1: #ponemos según las opciones un nombre y el valor de la cuenta
        product = "Fanta 600ml"
        bill = 340
    elif selection==2:
        product = "Coca-cola 600ml"
        bill = 400
    elif selection==3:
        product = "Sprite 600ml"
        bill = 340
    elif selection==4:
        product = "Coca-cola light 600ml"
        bill = 420
    elif selection==5:
        product = "Coca-cola zero 600ml"
        bill = 350
    elif selection==6:
        product = "Mundet 600ml"
        bill = 320
    elif selection==7:
        product = "Coca-cola cherry 420ml"
        bill = 300
    elif selection==8:
        product = "Coca-cola vainilla 420ml"
        bill = 300
    elif selection==9:
        product = "Monster 500ml"
        bill = 560
    else:# en caso que no coincida con una opción
        print("not valid option, select a number 1-9") #lo señalamos
        return list_of_coins_numbers #y devolvemos lo que metieron
    return change_of(bill,list_of_coins_numbers,[200,100,50,10,5],product) # en otro caso, ya usamos nuestra función
print(vendor_machine([1,0,0,0,0],5))
print(vendor_machine([2,0,0,0,0],2))