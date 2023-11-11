#al no pedir que hacer con el formato equivocado, se supondrá que el usuario ya conoce este formato, preocupandonos solo del resto
#partiremos del hecho que recibiremos cosas del tipo: [(a,b),(c,d),....], es decir, una lista con tuplas de dos
def correct_format(a_list):
    for i in range(len(a_list)):
        if type(a_list[i]) != tuple: #primero pedimos que cada elemento sea una tupla
            print("todas las entradas deben ser tuplas")
            return False
        elif len(a_list[i])!=2:#si cada entrada tiene longitud distinta de dos
            print("cada tupla solo debe tener dos elementos")
            return False#no cumple el formato
        elif not set(a_list[i]).issubset({"P","R","S"}): #como siguiente filtro:
            #si alguna de las tuplas contiene caracteres diferentes a los señalados
            print("Cada elemento de las tuplas solo pueden ser P(papel), S(tijeras) o R(piedra) ")
            return False
    return True #si pasó cada filtro, entonces devuelve True
a = [("P","S"),("S","P"),("R","S")]
def who_won_rps(a_list):
    if correct_format(a_list): #si cumple con el formato
        count = 0
        for element in a_list:
            if element[0]=="S" and element[1]=="P": # tijeras gana a papel
                count+=1 #aumentamos
            elif element[0]=="S" and element[1]=="R": #tijeras pierda contra roca
                count-=1 #restamos
            elif element[0]=="R" and element[1]=="S": #roca gana a tijeras
                count+=1#aumentamos
            elif element[0]=="R" and element[1]=="P": #roca pierda contra papel
                count-=1
            elif element[0]=="P" and element[1]=="S": #papel pierde contra tijeras
                count-=1
            elif element[0]=="P" and element[1]=="R": #papel gana a roca
                count+=1
            #si ocurre otro caso, no suma ni resta, se deja sin mención
        if count>0: #en caso que haya más victorias de la primera entrada
            print("Player 1 wins") #el ganador es el primer jugador
        elif count<0: #en caso que haya más derrotas de la primera entrada
            print("Player 2 wins") #el ganador es el segundo jugador
        else:
            print("Tie") #en otro caso, es un empate
who_won_rps(a) #aquí gana 1
a.append(("S","R")) #agregamos una victoria para 2
who_won_rps(a) #aquí empatamos
a.append(("S","S")) #agregamos un empate
who_won_rps(a) #sigue empatado
a.append(("S","R")) #agregamos una derrota
who_won_rps(a) #aquí gana 2
a.append(("S","T","T"))#agregamos una entrada incorrecta
who_won_rps(a) #nos señala que deben haber solo dos elementos
del a[-1]
a.append(("s","r")) #agregamos una entrada de dos elementos pero que no son correctos
who_won_rps(a) #nos señala que cada tupla solo debe tener elementos adecuados
del a[-1]
a.append("s")#agregamos un str
who_won_rps(a) #nos señala que deben ser tuplas en cada entrada

