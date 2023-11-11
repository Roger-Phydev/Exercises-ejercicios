import re
def capitalize_just_begin(my_string):
    patrn = r"[^a-zA-Záéíóú]" #el patrón que se usa es cualquier cosa distinta de letras
    my_string = " "+my_string#le pegamos un espacio en blanco al inicio para que funcione el siguiente código
    for i in range(1,len(my_string)):#para cada caracter
        if re.match(patrn,my_string[i-1])!=None and re.match(patrn,my_string[i])==None:#si el anterior no es una letra y el actual sí
            my_string = my_string.replace(my_string[i],my_string[i].upper())#sustituye su valor por mayúscula
    my_string = my_string[1:]#quitamos el " " que agregamos al inicio
    return my_string #devolvemos lo pedido
frase_1 = "hola mundo mortal maravilloso   quince"
print(capitalize_just_begin(capitalize_just_begin(frase_1)))