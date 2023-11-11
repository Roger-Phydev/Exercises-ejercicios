import re #usaremos expresiones regulares
def count_words(string):
    string = string.lower()#hacemos todo en minúsculas
    pattern = r"[^a-z0-9\s{1}]+" #nos fijaremos en  cosas que no sean letras, números o exactamente un espacio
    spaces = r"\s*" #si hay uno o más espacios
    while re.search(pattern,string)!=None:#mientras siga encontrandose patrones malos
        start,end = re.search(pattern,string).span() 
        string = string.replace(string[start:end],"")#quita lo que no debe estar
    string = string.split(" ")#usamos separadores
    while string.count("")>0:#mientras halla espacios en blanco
        string.remove("") #los remueve
    words = {} #creamos un diccionario donde guardar los datos
    for item in string:#para cada elemento restante
        words[item] = string.count(item) #creamos una entrada en el diccionario con su cantidad
    return words #devuelve el diccionario
frase = "Enefecto ..  si, en efecto, yo digo, que yo, estoy, en lo correcto. Esto porque yo soy       .......muy listo mientras estoy escribiendo"
print(count_words(frase))