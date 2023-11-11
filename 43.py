import random
grupo_truco = [["Adrian",12,156],["Josefa",9,134],["Luis",6,125],["Federico",9,160],["Luz",10,147]]
grupo_trato = [["Fabiola",10,132],["Alberto",3,85],["Luisa",6,110],["Ricardo",14,163],["Tatiana",11,150]]
def trick_or_treat(list_of_kids,trick):
    if type(list_of_kids)!=list:
        print("error, tu entrada debe ser una lista")
        return None
    for element in list_of_kids:
        if len(element)!=3:
            print("error, datos insuficientes en algún niño")
            return None
        if type(element[0])!=str or type(element[1])!=int or type(element[2])!=int:
            print("alguno de tus datos está equivocado, el formato es: nombre,edad(entero),altura(entero)")
            return None
    giveaway = [] #aqui guardamos lo que les daremos
    candies = [🍰,🍬,🍡,🍭,🍪,🍫,🧁,🍩] #creamos listas de dulces y sustos
    scares = [🎃,👻,💀,🕷,🕸,🦇]
    if trick == True: #si eligen truco
        number = 0 #este será el número de sustos por persona
        height = 0 #creamos variables para guardar lo que queremos
        for kid in list_of_kids: #para cada niño
            number+=len(kid[0])//2
            if kid[1]%2==0:
                number+=2
            giveaway.append([random.choice(scares) for i in range(number)])#agrega una lista con sustos al azar
            height+=kid[2]
        number=3*(height//100) #ahora modificamos el número, aumentará 3 por cada 100cm en altura
        for element in giveaway:
            element = element+[random.choice(scares) for i in range(number)]#añadimoas a cada lista los correspondientes a la altura total
        return giveaway
    elif trick == False:
        for kid in list_of_kids:
            n=len(kid[0])#aquí añadimos según cada letra
            if kid[1]<11: #si se tiene menos de 11 años
                n+=kid[1]//3 #un dulce por cada 3 años
            else:
                n+=3 #en caso contario, ya se aumentan 3
            if height<151:
                n+=height//50 #aumentamos cada 50 de altura
            else:
                n+=3 #en caso contario aumenta 3
            giveaway.append([random.choice(candies) for i in range(n)]) #añadimos los dulces adecuados
            return giveaway
    else:
        print("error, tu segundo argumento debe ser True si quieres truco o False si quieres trato")
print(trick_or_treat(grupo_truco,True))
