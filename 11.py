def del_char_in_common(str_1,str_2):
    char_1 = set(str_1) #creamos los conjuntos con los caracteres que hay en cada cadena
    char_2 = set(str_2)
    for item in char_2:#para cada elemento en char 2
        str_1 = str_1.replace(item,"") #lo reemplazamos por un vacío
    for item in char_1: #hacemos lo mismo con la otra cadena
        str_2 = str_2.replace(item,"")
    return [str_1,str_2]
a = "abcg"
b = "cdefg"
print(del_char_in_common(a,b)) 