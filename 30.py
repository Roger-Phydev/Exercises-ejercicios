#vamos a suponer que podemos separar las palabras con un espacio
def get_a_mark_for(an_string,marc_element="*"):
    an_string = an_string.split(" ")#separamos con espacios
    l = 0 #usaremos una variable para saber el largo que debemos usar
    for element in an_string:
        l = max(l,len(element)) #calculamos la máxima longitud de palabras de la cadena
    print(marc_element*((l//len(marc_element))+4)) #imprimimos la parte de arriba
    for element in an_string:
        print(marc_element+" "+element+" "*(l-len(element)+1)+marc_element)#para cada elemento creamos el marco
    print(marc_element*((l//len(marc_element))+4)) #cerramos el marco
frase = "por favor que alguien me ayude"
get_a_mark_for(frase) #marco de asteriscos
get_a_mark_for(frase,"#") #marco con gato
get_a_mark_for(frase,"::") #marco con otra cadena
frase_ejemplo = "¿Qué te parece el reto?"
get_a_mark_for(frase_ejemplo,"&")