import re
def is_palyndrom(my_string):
    my_string = my_string.lower()#hacemos todo minúsculas
    ptrn_1 = r"[^a-záéíóú]+" #nuestro primer patrón serán caracteres que no sean una letra con o sin acento
    ptrn_2 = r"[áéíóú]"#en el segundo, nos fijamos en las letras con acento
    while re.search(ptrn_1,my_string)!=None: #primero retiramos lo que no sean letras con o sin acento
        start,end = re.search(ptrn_1,my_string).span()
        my_string = my_string.replace(my_string[start:end],"") #para ello lo reemplazamos por vacíos
    while re.search(ptrn_2,my_string)!=None: #ahora nos deshacemos de las letras con acento
        start,end = re.search(ptrn_2,my_string).span() #las buscamos
        remain = my_string[start:end]#identificamos
        if remain == "á":#y según el caso las reemplazamos por su equivalente sin acento
            my_string = my_string.replace(remain,"a")
        elif remain == "é":
            my_string = my_string.replace(remain,"e")
        elif remain == "í":
            my_string = my_string.replace(remain,"i")
        elif remain == "ó":
            my_string = my_string.replace(remain,"o")
        elif remain == "ú":
            my_string = my_string.replace(remain,"u")
    my_string = list(my_string) #convertimos a lista para comparar
    rev_string = list(reversed(my_string)) #ahora creamos la lista invertida
    print(my_string)
    print(rev_string)
    if my_string == rev_string: #si coinciden
        return True #es verdadero0
    else: #caso contario
        return False #es falso
palindromo_1 = "áníta lava la tina"
palindromo_2 = "Aná llevá al Osó la avellana"
no_palindromo_1 = "alfa centauri ****"
no_palindromo_2 = "parece eceraq"
print(is_palyndrom(palindromo_1))
print(is_palyndrom(palindromo_2))
print(is_palyndrom(no_palindromo_1))
print(is_palyndrom(no_palindromo_2))